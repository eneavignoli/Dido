//libraries
#include <Stepper.h>

//pieces detection
const byte COLUMN[8] = {22,23,24,25,26,27,28,29};
const byte ROW[8] = {32,33,34,35,36,37,38,39};
//switches
const byte X_START_SWITCH_C = 17;
const byte X_START_SWITCH_O = 16;
const byte X_END_SWITCH_C = 14;
const byte X_END_SWITCH_O = 15;
const byte Y_START_SWITCH_C = 51;
const byte Y_START_SWITCH_O = 50;
const byte Y_END_SWITCH_C = 52;
const byte Y_END_SWITCH_O = 53;

const byte MAGNET_SWITCH = 4;

//motors
const long X_SPEED = 1000;
const byte X_PINDIR = 3;
const byte X_PINSTEP = 2;
const byte Y_MOTOR_STEPS = 200;
const byte Y_PHASE1 = 42;
const byte Y_PHASE2 = 43;
const byte Y_PHASE3 = 44;
const byte Y_PHASE4 = 45;
//linear movement for each step (1/16 of total right) in x axis
const float X_MOVE_PER_STEP = 20/200;
//linear movement for each step (1/200 of total right) in y axis
const float Y_MOVE_PER_STEP = 20/200;

//variables
int **chessBoard;
int **aiCemetery;
int **humanCemetery;
Stepper yStepper(Y_MOTOR_STEPS,Y_PHASE1,Y_PHASE2,Y_PHASE3,Y_PHASE4);

//functions
void setupBoard(int **board, int **aiCem, int **humanCem);
void readBoard(int **board);
void printBoard(int **board);
bool isXToZero();
bool isXToEnd();
bool isYToZero();
bool isYToEnd();
void stepperXToZero();
void stepperXToEnd();
void stepperYToZero();
void stepperYToEnd();
void movePiece(byte i_zone,byte i_row,byte i_column,byte d_zone,byte d_row,byte d_column);
void setupAIPieces();
char receiveFromRasp();

void setup() {
  //setup switches pins
  pinMode(X_START_SWITCH_C,INPUT_PULLUP);
  pinMode(X_START_SWITCH_O,INPUT_PULLUP);
  pinMode(X_END_SWITCH_C,INPUT_PULLUP);
  pinMode(X_END_SWITCH_O,INPUT_PULLUP);
  pinMode(Y_START_SWITCH_C,INPUT_PULLUP);
  pinMode(Y_START_SWITCH_O,INPUT_PULLUP);
  pinMode(Y_END_SWITCH_C,INPUT_PULLUP);
  pinMode(Y_END_SWITCH_O,INPUT_PULLUP);
  
  pinMode(MAGNET_SWITCH,OUTPUT);
  
  //setup motor pins
  pinMode(X_PINSTEP,OUTPUT);
  pinMode(X_PINDIR,OUTPUT);
  pinMode(Y_PHASE1,OUTPUT);
  pinMode(Y_PHASE2,OUTPUT);
  pinMode(Y_PHASE3,OUTPUT);
  pinMode(Y_PHASE4,OUTPUT);
  
  //set y stepper rpm
  yStepper.setSpeed(100);
  
  //setup detection pins
  for(int i = 0; i < 8; i++){
    pinMode(COLUMN[i],INPUT_PULLUP);
    pinMode(ROW[i],OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  char start = 'F';
  do{
    start = receiveFromRasp();
  }while(start != 'S');
  setupAIPieces();
  delay(10000);
}

void setupBoard(int **board, int **aiCem, int **humanCem){
  //istance the matrix
  board = new int*[8];
  aiCem = new int*[8];
  humanCem = new int*[8];
  
  for(int i = 0; i < 8; i++){
    board[i] = new int[8];
    aiCem[i] = new int[2];
    humanCem[i] = new int[2];
  }

  //initialize the matrix
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(i < 2 || i > 5){
        board[i][j] = 1;
        aiCem[i][j] = 0;
        humanCem[i][j] = 0;
      }
      else{
        board[i][j] = 0;
      }
    }
  }
}

void readBoard(int **board){
  //security setup -> all rows switched off
  for(int i = 0; i < 8; i++){
    digitalWrite(ROW[i],1);;
  }

  for(int i = 0; i < 8; i++){
    //switch on the row
    digitalWrite(ROW[i],0);
    //wait a little bit
    delay(10);
    //read all columns
    for(int j = 0; j < 8; j++){
      int tempRead;
      //read the column and put in the temporary variable
      tempRead = digitalRead(COLUMN[j]);
      //read confirmation after a 1/2 second
      if(tempRead != board[i][j]){
        delay(100);
        board[i][j] = digitalRead(COLUMN[j]);
      }
    }
    //switch off the row
    digitalWrite(ROW[i],1);
  }
}

void printBoard(int **board){
  for(int row = 0; row < 8; row++){
    for(int column = 0; column < 8; column ++){
      String stamp = " ";
      if(board[row][column] == 1)
        stamp += "1";
      else
        stamp += "0";
      stamp += " |";
      Serial.print(stamp);
    }
    Serial.println();
    Serial.println("---------------------------------");
  }
}

bool isXToZero(){
  if(digitalRead(X_START_SWITCH_O) == 0)
    return true;
  else
    return false;
}

bool isXToEnd(){
  if(digitalRead(X_END_SWITCH_O) == 0)
    return true;
  else
    return false;
}

bool isYToZero(){
  if(digitalRead(Y_START_SWITCH_O) == 0)
    return true;
  else
    return false;
}

bool isYToEnd(){
  if(digitalRead(Y_END_SWITCH_O) == 0)
    return true;
  else
    return false;
}

void stepperYToZero(){
  while(!isYToZero())
    yStepper.step(1);
}

void stepperYToEnd(){
  while(!isYToEnd())
    yStepper.step(-1);
}

void stepperXToZero(){
  //define direction
  digitalWrite(X_PINDIR,HIGH);
  //step
  while(!isXToZero()){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
}

void stepperXToEnd(){
  //define direction
  digitalWrite(X_PINDIR,LOW);
  //step
  while(!isXToEnd()){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
}

void movePiece(byte i_zone,byte i_row,byte i_column,byte d_zone,byte d_row,byte d_column){
  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToEnd();
  int steps = 11 / Y_MOVE_PER_STEP;
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }

  //move to the piece square
  //0 = ai cem 1 = board 2 = human cem
  switch(i_zone){
    case 0:
      steps = i_column * 50 / X_MOVE_PER_STEP;
      break;
    case 1:
      steps = (140 + i_column + 70) / X_MOVE_PER_STEP;
      break;
    case 2:
      steps = (140 + 560 + i_column * 50) / X_MOVE_PER_STEP;
      break;
  }
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  return;
  steps = i_row * 70 / Y_MOVE_PER_STEP;
  
  for(int i = 0; i <= steps and !isYToZero(); i++){
    yStepper.step(1);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);

  //now move to the destination square
  if(i_row > d_row){
    steps = 35 / Y_MOVE_PER_STEP;
    for(int i = 0; i <= steps and !isYToEnd(); i++){
      yStepper.step(-1);
    }
  }
  else
  {
    if(i_row < d_row){
      steps = 35 / Y_MOVE_PER_STEP;
      for(int i = 0; i <= steps and !isYToZero(); i++){
        yStepper.step(1);
      }
    }
    else{
      if(i_row > 0){
        steps = 35 / Y_MOVE_PER_STEP;
        for(int i = 0; i <= steps and !isYToZero(); i++){
          yStepper.step(1);
        }
      }
      else{
        steps = 35 / Y_MOVE_PER_STEP;
        for(int i = 0; i <= steps and !isYToZero(); i++){
          yStepper.step(-1);
        }
      }
    }
  }
  
  if(i_zone == d_zone){
    if(i_column > d_column){
      digitalWrite(X_PINDIR,HIGH);
      steps = ((i_column - d_column -1) * 70) / X_MOVE_PER_STEP;
      for(int i = 0; i <= steps and !isXToZero(); i++){
        digitalWrite(X_PINSTEP,HIGH);
        delayMicroseconds(X_SPEED);
        digitalWrite(X_PINSTEP,LOW);
        delayMicroseconds(X_SPEED);
      }
    }
    else{
      if(i_column == d_column){
        if(i_row > 0){
          digitalWrite(X_PINDIR,LOW);
        }
        else{
          digitalWrite(X_PINDIR,HIGH);
        }
        steps = 35 / X_MOVE_PER_STEP;
        for(int i = 0; i <= steps and !isXToZero() and !isXToEnd(); i++){
          digitalWrite(X_PINSTEP,HIGH);
          delayMicroseconds(X_SPEED);
          digitalWrite(X_PINSTEP,LOW);
          delayMicroseconds(X_SPEED);
        }
      }
      else{
        digitalWrite(X_PINDIR,LOW);
        steps = ((d_column - i_column -1) * 70) / X_MOVE_PER_STEP;
        for(int i = 0; i <= steps and !isXToEnd(); i++){
          digitalWrite(X_PINSTEP,HIGH);
          delayMicroseconds(X_SPEED);
          digitalWrite(X_PINSTEP,LOW);
          delayMicroseconds(X_SPEED);
        }
      }
    }
  }
  else{
    if(i_zone == 0){
      if(d_zone == 1){
        steps = ((140 - i_column * 45) + d_column * 70) / X_MOVE_PER_STEP;
        digitalWrite(X_PINDIR,LOW);
        for(int i = 0; i <= steps and !isXToEnd(); i++){
          digitalWrite(X_PINSTEP,HIGH);
          delayMicroseconds(X_SPEED);
          digitalWrite(X_PINSTEP,LOW);
          delayMicroseconds(X_SPEED);
        }
      }
      else{
        if(d_zone == 2){
          steps = ((140 - i_column * 45) + 70 * 7 + d_column * 45 + 95) / X_MOVE_PER_STEP;
          digitalWrite(X_PINDIR,LOW);
          for(int i = 0; i <= steps and !isXToEnd(); i++){
            digitalWrite(X_PINSTEP,HIGH);
            delayMicroseconds(X_SPEED);
            digitalWrite(X_PINSTEP,LOW);
            delayMicroseconds(X_SPEED);
          }
        }
      }
    }
    else{
      if(i_zone == 1){
        if(d_zone == 0){
          steps = (i_column - 1) * 70 + 95;
          if(d_column == 0)
            steps += 45;
          digitalWrite(X_PINDIR,HIGH);
          for(int i = 0; i <= steps and !isXToZero(); i++){
            digitalWrite(X_PINSTEP,HIGH);
            delayMicroseconds(X_SPEED);
            digitalWrite(X_PINSTEP,LOW);
            delayMicroseconds(X_SPEED);
          }
        }
        else{
          if(d_zone == 2){
            steps = ((i_column - 1) * 70 + d_column * 45 + 95) / X_MOVE_PER_STEP;
            digitalWrite(X_PINDIR,LOW);
            for(int i = 0; i <= steps and !isXToEnd(); i++){
              digitalWrite(X_PINSTEP,HIGH);
              delayMicroseconds(X_SPEED);
              digitalWrite(X_PINSTEP,LOW);
              delayMicroseconds(X_SPEED);
            }
          }
        }
      }
      else{
        if(i_zone == 2){
          if(d_zone == 0){
            steps = (i_column - 1) * 70 + 95;
            if(d_column == 0)
              steps += 45;
            digitalWrite(X_PINDIR,HIGH);
            for(int i = 0; i <= steps and !isXToZero(); i++){
              digitalWrite(X_PINSTEP,HIGH);
              delayMicroseconds(X_SPEED);
              digitalWrite(X_PINSTEP,LOW);
              delayMicroseconds(X_SPEED);
            }
          }
          else{
            if(d_zone == 1){
              steps = ((7 - i_column) * 70 + d_column * 45 + 95) / X_MOVE_PER_STEP;
              digitalWrite(X_PINDIR,LOW);
              for(int i = 0; i <= steps and !isXToEnd(); i++){
                digitalWrite(X_PINSTEP,HIGH);
                delayMicroseconds(X_SPEED);
                digitalWrite(X_PINSTEP,LOW);
                delayMicroseconds(X_SPEED);
              }
            }
          }
        }
      }
    }
  }

  //up, down, left or right
  
  //move to setup position
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);
}

void setupAIPieces(){
  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  int steps = 120;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 7;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);

  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  steps = 120 + 350;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 6;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  
  steps = 350;
  
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }
  
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);

  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  steps = 120 + 350 * 2;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 5;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  
  steps = 350 * 2;
  
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }
  
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);

  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  steps = 120 + 350 * 3;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 4;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  
  steps = 350 * 3;
  
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }
  
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);

  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  steps = 120 + 350 * 4;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 3;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  
  steps = 350 * 4;
  
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }
  
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);

  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  steps = 120 + 350 * 5;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 2;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  
  steps = 350 * 5;
  
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }
  
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);

  //move to first cemetery position - setup position
  stepperXToZero();
  stepperYToZero();
  steps = 120 + 350 * 6;
  for(int i = 0; i <= steps and (!isYToEnd()); i++){
    yStepper.step(-1);
  }

  //move to the piece square
  steps = 200;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }

  //switch the electromagnet on
  digitalWrite(MAGNET_SWITCH,HIGH);
  //move to the destination square
  steps = 475 + 350 * 1;
  
  digitalWrite(X_PINDIR,LOW);
  for(int i = 0; i <= steps and !isXToEnd(); i++){
    digitalWrite(X_PINSTEP,HIGH);
    delayMicroseconds(X_SPEED);
    digitalWrite(X_PINSTEP,LOW);
    delayMicroseconds(X_SPEED);
  }
  
  steps = 350 * 6;
  
  for(int i = 0; i <= steps and (!isYToZero()); i++){
    yStepper.step(1);
  }
  
  //switch the electromagnet off
  digitalWrite(MAGNET_SWITCH,LOW);
}

char receiveFromRasp(){
  char incomingByte = '0';
  while(true){
    if(Serial.available() > 0){
      incomingByte = Serial.read();
      return incomingByte;
    }
  }
}


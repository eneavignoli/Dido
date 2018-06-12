//libraries
#include <Stepper.h>

//pieces detection
const byte COLUMN[8] = {22,23,24,25,26,27,28,29};
const byte ROW[8] = {32,33,34,35,36,37,38,39};
//switches
const byte X_START_SWITCH_C = 16;
const byte X_START_SWITCH_O = 17;
const byte X_END_SWITCH_C = 14;
const byte X_END_SWITCH_O = 15;
const byte Y_START_SWITCH_C = 50;
const byte Y_START_SWITCH_O = 51;
const byte Y_END_SWITCH_C = 52;
const byte Y_END_SWITCH_O = 53;
//motors
const byte X_MOTOR_STEPS = 64;
const byte X_PHASE1 = 18;
const byte X_PHASE2 = 19;
const byte X_PHASE3 = 20;
const byte X_PHASE4 = 21;
const byte Y_MOTOR_STEPS = 200;
const byte Y_PHASE1 = 42;
const byte Y_PHASE2 = 43;
const byte Y_PHASE3 = 44;
const byte Y_PHASE4 = 45;

//variables
int **chessBoard;
Stepper yStepper(Y_MOTOR_STEPS,Y_PHASE1,Y_PHASE2,Y_PHASE3,Y_PHASE4);
Stepper xStepper(X_MOTOR_STEPS,X_PHASE1,X_PHASE2,X_PHASE3,X_PHASE4);

//functions
void readBoard(int **board);
void readBoard(int **board);
void printBoard(int **board);
bool isXToZero();
bool isXToEnd();
bool isYToZero();
bool isYToEnd();
void stepperXToZero();
void stepperYToZero();

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
  
  //set x stepper rpm
  xStepper.setSpeed(100);
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
  Serial.println("Inizio Corsa X: " + isXToZero());
  Serial.println("Fine Corsa X: " + isXToEnd());
  Serial.println("Inizio Corsa Y: " + isYToZero());
  Serial.println("Inizio Corsa Y: " + isYToEnd());
  delay(2000);
//  readBoard(chessBoard);
//  printBoard(chessBoard);
//  delay(10000);
}

void setupBoard(int **board){
  //istance the matrix
  board = new int*[8];
  for(int i = 0; i < 8; i++){
    board[i] = new int[8];
  }
  //initialize the matrix
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(i < 2 || i > 5)
        board[i][j] = 1;
      else
        board[i][j] = 0;
    }
  }
}

void readBoard(int **board){
//  //security setup -> all row switched off
//  for(int i = 0; i < 8; i++){
//    digitalWrite(ROW[i],1);;
//  }
//
//  for(int i = 0; i < 8; i++){
//    //switch on the row
//    digitalWrite(ROW[i],0);
//    //wait a little bit
//    delay(50);
//    //read all columns
//    for(int j = 0; j < 8; j++){
//      int tempRead;
//      //read the column and put in the temporary variable
//      tempRead = digitalRead(COLUMN[j]);
//      //read confirmation after a 1/2 second
//      if(tempRead != board[i][j]){
//        delay(500);
//        board[i][j] = digitalRead(COLUMN[j]);
//      }
//    }
//    //switch off the row
//    digitalWrite(ROW[i],1);
//  }
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


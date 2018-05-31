//libraries
#include <Stepper.h>

//costants
const byte COLUMN[8] = {22,23,24,25,26,27,28,29};
const byte ROW[8] = {32,33,34,35,36,37,38,39};
const byte MOTOR_STEPS = 200;
const byte PHASE1 = 42;
const byte PHASE2 = 43;
const byte PHASE3 = 44;
const byte PHASE4 = 45;

//variables
int **chessBoard;
Stepper bigStepper(MOTOR_STEPS,PHASE1,PHASE2,PHASE3,PHASE4);

//functions
void readBoard(int **board);
void readBoard(int **board);
void printBoard(int **board);

void setup() {
  //set bigger stepper rpm
  bigStepper.setSpeed(100);
  //setup pins
  for(int i = 0; i < 8; i++){
    pinMode(COLUMN[i],INPUT_PULLUP);
    pinMode(ROW[i],OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  bigStepper.step(4000);
  delay(5000);
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
  //security setup -> all row switched off
  for(int i = 0; i < 8; i++){
    digitalWrite(ROW[i],1);;
  }

  for(int i = 0; i < 8; i++){
    //switch on the row
    digitalWrite(ROW[i],0);
    //wait a little bit
    delay(50);
    //read all columns
    for(int j = 0; j < 8; j++){
      int tempRead;
      //read the column and put in the temporary variable
      tempRead = digitalRead(COLUMN[j]);
      //read confirmation after a 1/2 second
      if(tempRead != board[i][j]){
        delay(500);
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


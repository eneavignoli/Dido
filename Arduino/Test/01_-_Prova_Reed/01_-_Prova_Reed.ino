//pin digitale a cui è collegato "data"  
const byte pin_reed = 22;
//esito della lettura digitale
bool magnete = false;

void setup() {
  
  Serial.begin(9600);
  Serial.println("Inizio Rilevamento");

  pinMode(pin_reed,INPUT_PULLUP);
}

void loop() {
  
  magnete = digitalRead(pin_reed);
  
  if (magnete == true)
  {
    Serial.println("NO");
  }
  else
  {
    Serial.println("SI");
  }

  delay(500);
}

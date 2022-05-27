// Arduino pin numbers
const int Dedo0 = 2; 
const int Dedo1 = 3; 
const int Dedo2 = 4; 
const int Dedo3 = 5; 
const int Dedo4 = 6;
const int Send = 7; 

int posicion = 0;

const int tiempo_delay = 20; // Tiempo de delay despues de una lectura

void setup() {
  Serial.begin(9600);
  pinMode(Dedo0,INPUT_PULLUP);
  pinMode(Dedo1,INPUT_PULLUP);
  pinMode(Dedo2,INPUT_PULLUP);
  pinMode(Dedo3,INPUT_PULLUP);
  pinMode(Dedo4,INPUT_PULLUP);
  pinMode(Send,INPUT_PULLUP);
}

void loop() {

if(digitalRead(Send) != HIGH){
  delay(tiempo_delay);
  posicion = 0;
  if(digitalRead(Dedo0) != HIGH){
  posicion += 1;
  }
  if(digitalRead(Dedo1) != HIGH){
  posicion += 2;
  }
  if(digitalRead(Dedo2) != HIGH){
  posicion += 4;
  }
  if(digitalRead(Dedo3) != HIGH){
  posicion += 8;
  }
  if(digitalRead(Dedo4) != HIGH){
  posicion += 16;
  }
  Serial.println(posicion);
  while(digitalRead(Send) != HIGH){
    delay(tiempo_delay);}
} 
 

}

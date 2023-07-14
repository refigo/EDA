#include <Encoder.h>

Encoder myEncL(2, 22);
Encoder myEncR(3, 23);

void setup() {
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
}

long oldPositionL = -999;
long oldPositionR = -999;

void loop() {
  long newPositionL = myEncL.read();
  long newPositionR = myEncR.read();

  bool condi = (newPositionL != oldPositionL) || (newPositionR != oldPositionR);
  
  if (condi==true) {
    oldPositionL = newPositionL;
    oldPositionR = newPositionR;
    
    Serial.print(oldPositionL);
    Serial.print(", ");
    Serial.println(oldPositionR);
  }
}
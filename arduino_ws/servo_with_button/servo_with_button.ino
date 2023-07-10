#include <Servo.h>

Servo servo;
int pos = 0;
int push_button = 2;
bool to_up = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  pinMode(push_button, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(push_button)==HIGH) {
    if (to_up == true) {
      pos += 10;
      if (pos >= 180) {
        to_up = false;
        pos = 180;
      }
    } else {
      pos -= 10;
      if (pos <= 0) {
        to_up = true;
        pos = 0;
      }
    }

    Serial.print("pos: ");
    Serial.println(pos);

    servo.write(pos);
    delay(100);
  }
}

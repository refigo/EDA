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


// Example for servo motor with button
/*
#include <Servo.h>
int pos = 0;
int push_btn = 2;
bool flag = 0;
bool dir = 0;
Servo servo;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(push_btn, INPUT);
  servo.attach(9);
}
void loop() {
  // put your main code here, to run repeatedly:
  bool incoming_data = digitalRead(push_btn);
  if(incoming_data==HIGH & flag==0){
    Serial.println("Button is pressed.");
    flag = 1;
    // rotate
    if(dir == 0) {
      pos += 10;
    }
    else {
      pos -= 10;
    }
    servo.write(pos);
    // check if dir need to be changed
    if(pos >= 180 || pos <= 0) {
      dir = !dir;
    }
  }
  if(incoming_data==LOW & flag==1){
    Serial.println("---");
    flag = 0;
  }
}
*/

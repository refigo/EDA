const int ledPinR = 6;
const int ledPinL = 44;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPinR, OUTPUT);
  pinMode(ledPinL, OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPinR, HIGH);
  digitalWrite(ledPinL, LOW);
  delay(500);
  digitalWrite(ledPinL, HIGH);
  digitalWrite(ledPinR, LOW);
  delay(500);
}

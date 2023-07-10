const int LED = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  int light = analogRead(A0);

  int out = map(light, 50, 200, 0, 250);

  Serial.println(out);
  if (out < 0) {
    out = 0;
  }
  
  if (out > 250) {
    out = 250;
  }

  Serial.print(light);
  Serial.print(", ");
  Serial.println(out);

  analogWrite(LED, out);
}

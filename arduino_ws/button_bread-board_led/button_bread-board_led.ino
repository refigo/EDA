int push_button = 2;
bool flag = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(push_button, INPUT);
  Serial.println("Hello. Ready!!!");
}

void loop() {
  // put your main code here, to run repeatedly:
  bool incomming_data = digitalRead(push_button);
  if (incomming_data==HIGH) {
    digitalWrite(LED_BUILTIN, HIGH);
    if (flag==0) {
      Serial.println("Button is pressed.");
      flag = 1;
    }

  }
  if (incomming_data==LOW) {
    digitalWrite(LED_BUILTIN, LOW);
    if (flag==1) {
      Serial.println("---");
      flag = 0;
    }
    
  }
}

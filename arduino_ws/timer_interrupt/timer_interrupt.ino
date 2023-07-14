const int ledPinR = 6;
const int ledPinL = 44;

int cnt = 1;

void setup() {
  // put your setup code here, to run once:
  // Timer: Control loop
  Serial.begin(115200);
  pinMode(ledPinR, OUTPUT);
  pinMode(ledPinL, OUTPUT);

  cli();
  TCCR4A = 0; // set entire TCCR4A register to 0
  TCCR4B = 0; // set entire TCCR4B register to 0
  TCNT4 = 0; // initialize counter value to 0

  OCR4A = 312; //= (16MHz) / (50Hz*1024) - 1 (must be <65536)

  TCCR4B |= (1 << WGM12);
  TCCR4B |= (1 << CS12) | (1 << CS10);
  TIMSK4 |= (1 << OCIE4A);
  
  sei();
}

void loop() {
  // put your main code here, to run repeatedly:

}

ISR(TIMER4_COMPA_vect) {
  if (cnt<50) {
    cnt++;
    //Serial.println(cnt);
  } else {
    Serial.println(cnt);
    cnt = 0;
  }
  
}
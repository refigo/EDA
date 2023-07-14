#include <Encoder.h>
#include <ArduPID.h>

#define R_MOTOR_IN1 7
#define R_MOTOR_IN2 8
#define R_MOTOR_PWM 13

#define L_MOTOR_IN1 10
#define L_MOTOR_IN2 11
#define L_MOTOR_PWM 12

#define MOTOR_STBY 9

#define R_ENC_A 3
#define R_ENC_B 23

#define L_ENC_A 2
#define L_ENC_B 22

// Motor Related
uint8_t g_motor_enabled = 0;

uint8_t g_r_lamp_val = 0;
int16_t g_r_motor_target = 0;
int32_t g_r_current_encoder = 0;
int32_t g_r_last_encoder = 0;

uint8_t g_l_lamp_val = 0;
int16_t g_l_motor_target = 0;
int32_t g_l_current_encoder = 0;
int32_t g_l_last_encoder = 0;

uint16_t g_range_sensor_val = 0;

// PID Related
double r_current_vel = 0;
double r_control_output = 0;
double r_target_vel = 0;

double l_current_vel = 0;
double l_control_output = 0;
double l_target_vel = 0;

double p_gain = 6;
double i_gain = 2;
double d_gain = 0.2;

ArduPID r_motor_controller;
ArduPID l_motor_controller;

int32_t old_r_enc = 0;
Encoder r_enc(R_ENC_A, R_ENC_B);

int32_t old_l_enc = 0;
Encoder l_enc(L_ENC_A, L_ENC_B);

int cnt = 1;

void setup() {
  // put your setup code here, to run once:
  // Timer: Control loop
  Serial.begin(115200);

  pinMode(R_MOTOR_IN1, OUTPUT);
  pinMode(R_MOTOR_IN2, OUTPUT);
  pinMode(R_MOTOR_PWM, OUTPUT);
  pinMode(L_MOTOR_IN1, OUTPUT);
  pinMode(L_MOTOR_IN2, OUTPUT);
  pinMode(L_MOTOR_PWM, OUTPUT);
  pinMode(MOTOR_STBY, OUTPUT);

  digitalWrite(MOTOR_STBY, HIGH);

  // Initialize
  g_motor_enabled = 0;

  g_r_lamp_val = 0;
  g_r_motor_target = 0;
  g_r_current_encoder = 0;
  g_r_last_encoder = 0;
  
  g_l_lamp_val = 0;
  g_l_motor_target = 0;
  g_l_current_encoder = 0;
  g_l_last_encoder = 0;

  g_range_sensor_val = 0;

  r_enc.write(0);
  l_enc.write(0);

  cli();
  TCCR4A = 0; // set entire TCCR4A register to 0
  TCCR4B = 0; // set entire TCCR4B register to 0
  TCNT4 = 0; // initialize counter value to 0

  OCR4A = 312; //= (16MHz) / (50Hz*1024) - 1 (must be <65536)
  
  TCCR4B |= (1 << WGM12);
  TCCR4B |= (1 << CS12) | (1 << CS10);
  TIMSK4 |= (1 << OCIE4A);

  sei();

  r_motor_controller.begin(&r_current_vel, &r_control_output, &r_target_vel, p_gain, i_gain, d_gain);
  r_motor_controller.setOutputLimits(-255, 255);
  r_motor_controller.setDeadBand(-10, 10);
  r_motor_controller.setWindUpLimits(-10, 10);
  
  l_motor_controller.begin(&l_current_vel, &l_control_output, &l_target_vel, p_gain, i_gain, d_gain);
  l_motor_controller.setOutputLimits(-255, 255);
  l_motor_controller.setDeadBand(-10, 10);
  l_motor_controller.setWindUpLimits(-10, 10);
  
  r_motor_controller.start();
  l_motor_controller.start();
}
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    String incommingStr = Serial.readString();
    int ws_idx = incommingStr.indexOf(" ");
    String first_num = incommingStr.substring(0, ws_idx);
    String second_num = incommingStr.substring(ws_idx+1);
    g_r_motor_target = first_num.toFloat();
    g_l_motor_target = second_num.toFloat();
  }

  Serial.print(String(g_r_motor_target));
  Serial.print(", ");
  Serial.println(String(r_current_vel, 3));

  Serial.print(String(g_l_motor_target));
  Serial.print(", ");
  Serial.println(String(l_current_vel, 3));
}

ISR(TIMER4_COMPA_vect) {

  g_r_current_encoder = r_enc.read();
  r_current_vel = g_r_current_encoder - g_r_last_encoder;
  g_r_last_encoder = g_r_current_encoder;

  g_l_current_encoder = l_enc.read();
  l_current_vel = g_l_current_encoder - g_l_last_encoder;
  g_l_last_encoder = g_l_current_encoder;

  digitalWrite(MOTOR_STBY, HIGH);
  
  r_target_vel = g_r_motor_target / 50.0;
  r_motor_controller.compute();
  if(r_control_output >= 0)
  {
    digitalWrite(R_MOTOR_IN1, HIGH);
    digitalWrite(R_MOTOR_IN2, LOW);
    analogWrite(R_MOTOR_PWM, r_control_output);
  }
  else {
    digitalWrite(R_MOTOR_IN1, LOW);
    digitalWrite(R_MOTOR_IN2, HIGH);
    analogWrite(R_MOTOR_PWM, -1 * r_control_output);
  }

  l_target_vel = g_l_motor_target / 50.0;
  l_motor_controller.compute();
  if(l_control_output >= 0)
  {
    digitalWrite(L_MOTOR_IN1, HIGH);
    digitalWrite(L_MOTOR_IN2, LOW);
    analogWrite(L_MOTOR_PWM, l_control_output);
  }
  else {
    digitalWrite(L_MOTOR_IN1, LOW);
    digitalWrite(L_MOTOR_IN2, HIGH);
    analogWrite(L_MOTOR_PWM, -1 * l_control_output);
  }
}
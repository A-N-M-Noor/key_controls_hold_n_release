#define m1p1 2
#define m1p2 3
#define m2p1 4
#define m2p2 5
#define m3p1 6
#define m3p2 7
#define m4p1 8
#define m4p2 9

byte pwmValue = 255;

void setup() {
  // Initialize motor control pins as outputs
  pinMode(m1p1, OUTPUT);
  pinMode(m1p2, OUTPUT);
  pinMode(m2p1, OUTPUT);
  pinMode(m2p2, OUTPUT);
  pinMode(m3p1, OUTPUT);
  pinMode(m3p2, OUTPUT);
  pinMode(m4p1, OUTPUT);
  pinMode(m4p2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {
    byte cmd = Serial.read();
    
    switch (cmd) {
      case 1:
        // forward
        Serial.println("Forward");
        analogWrite(m1p1, pwmValue);
        analogWrite(m1p2, 0);
        analogWrite(m2p1, pwmValue);
        analogWrite(m2p2, 0);
        analogWrite(m3p1, pwmValue);
        analogWrite(m3p2, 0);
        analogWrite(m4p1, pwmValue);
        analogWrite(m4p2, 0);
        break;
      case 2:
        // backwards
        Serial.println("Backwards");
        analogWrite(m1p1, 0);
        analogWrite(m1p2, pwmValue);
        analogWrite(m2p1, 0);
        analogWrite(m2p2, pwmValue);
        analogWrite(m3p1, 0);
        analogWrite(m3p2, pwmValue);
        analogWrite(m4p1, 0);
        analogWrite(m4p2, pwmValue);
        break;
      case 3:
        // right
        Serial.println("Right");
        analogWrite(m1p1, pwmValue);
        analogWrite(m1p2, 0);
        analogWrite(m2p1, 0);
        analogWrite(m2p2, pwmValue);
        analogWrite(m3p1, pwmValue);
        analogWrite(m3p2, 0);
        analogWrite(m4p1, 0);
        analogWrite(m4p2, pwmValue);
        break;
      case 4:
        // left
        Serial.println("Left");
        analogWrite(m1p1, 0);
        analogWrite(m1p2, pwmValue);
        analogWrite(m2p1, pwmValue);
        analogWrite(m2p2, 0);
        analogWrite(m3p1, 0);
        analogWrite(m3p2, pwmValue);
        analogWrite(m4p1, pwmValue);
        analogWrite(m4p2, 0);
        break;
      default:
        // 0, or unknown; stop
        Serial.println("Stop");
        analogWrite(m1p1, 0);
        analogWrite(m1p2, 0);
        analogWrite(m2p1, 0);
        analogWrite(m2p2, 0);
        analogWrite(m3p1, 0);
        analogWrite(m3p2, 0);
        analogWrite(m4p1, 0);
        analogWrite(m4p2, 0);
        break;
    }
  }
}

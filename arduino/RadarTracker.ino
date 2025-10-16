// RadarTracker.ino
// Simple scanning radar using HC-SR04 + SG90 servo on Arduino.
// Prints lines like: Angle: 45 Distance: 23.5 cm

#include <Servo.h>

Servo myServo;
const int trigPin = 9;
const int echoPin = 10;
const int servoPin = 11;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // Move to starting position
  myServo.write(0);
  delay(500);
}

float measureDistanceCM() {
  long duration;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH, 30000); // timeout 30 ms
  if (duration == 0) return -1; // no echo / out of range
  float distance = (duration / 2.0) / 29.1;
  return distance;
}

void loop() {
  // Sweep from 0 to 180 degrees and back
  for (int angle = 0; angle <= 180; angle += 2) {
    myServo.write(angle);
    delay(70); // allow servo to reach position
    float d = measureDistanceCM();
    if (d < 0) {
      Serial.print("Angle: ");
      Serial.print(angle);
      Serial.println(" Distance: -1 cm");
    } else {
      Serial.print("Angle: ");
      Serial.print(angle);
      Serial.print(" Distance: ");
      Serial.print(d, 1);
      Serial.println(" cm");
    }
    delay(30);
  }
  for (int angle = 180; angle >= 0; angle -= 2) {
    myServo.write(angle);
    delay(70);
    float d = measureDistanceCM();
    if (d < 0) {
      Serial.print("Angle: ");
      Serial.print(angle);
      Serial.println(" Distance: -1 cm");
    } else {
      Serial.print("Angle: ");
      Serial.print(angle);
      Serial.print(" Distance: ");
      Serial.print(d, 1);
      Serial.println(" cm");
    }
    delay(30);
  }
}

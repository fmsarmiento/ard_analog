#define SW_pin 2
#define X_pin 0
#define Y_pin 1

void setup() {
  // put your setup code here, to run once:
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(digitalRead(SW_pin)); // switch
  Serial.print("|");
  Serial.print(analogRead(X_pin)); // x axis
  Serial.print("|");
  Serial.println(analogRead(Y_pin)); // y axis
  delay(10);
}

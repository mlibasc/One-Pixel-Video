//This program is to collect data given by the photoresistor

int photoresistor = A0;
float val = 0;
float volt = 0;
const int vdd = 5;
const int max_bit = 1023;
float resistance = 0;
float r1 = 22000; 

void setup() {
  Serial.begin(9600);
}

void loop() {
  val = analogRead(photoresistor);
  volt = val * vdd / max_bit; 
  resistance = (r1*volt)/(vdd - volt);
  Serial.print("val = ");
  Serial.println(val);
  Serial.print("voltage = " );
  Serial.println(volt);
  Serial.print("resistor = ");
  Serial.println(resistance);
  delay(1000);
}

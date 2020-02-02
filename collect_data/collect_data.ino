//This program is to collect data given by the photoresistor

int photoresistor = A0;
int pushButton = A1;
float val = 0;
float volt = 0;
bool button = false; 
bool recording = false;
const int vdd = 5;
const int max_bit = 1023;
float resistance = 0;
float r1 = 22000;  
int i = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  val = analogRead(photoresistor);
  button = (analogRead(pushButton) < 500);
  volt = val * vdd / max_bit; 
  resistance = (r1*volt)/(vdd - volt);

  if(button || recording){
    recording = true;
    Serial.print(resistance);
    Serial.print(',');
    i++;
    if(i == 50){
      recording = false; 
      i = 0;
    }
  }
//  Serial.print("val = ");
//  Serial.println(val);
//  Serial.print("voltage = " );
//  Serial.println(volt);
//  Serial.print("resistor = ");
//  Serial.println(resistance);
//  Serial.println(button);
  delay(100);
}

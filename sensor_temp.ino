float voltageSensor=0;

void setup(){
    Serial.begin(9600);
    pinMode(13,OUTPUT);
}

void loop(){
    float valueSensor = analogRead(A0);
    float tempC = valueSensor/1023 * voltageSensor * 100;
    digitax lWrite(13, HIGHT);
    Serial.println(String(tempC));
    delay(1000);
}
# 1 "c:\\Users\\matth\\OneDrive - University of Prince Edward Island\\XAC Management and Storage\\_Freedom Wing Project\\Latency_Tester\\LatencyTester.cpp"

int currentLight = 0;
int pastLight = 0;
int buttonTime = 0;
int lightTime = 0;
int button = 0;
void setup()
{
 pinMode(A0, 0x0);
    pinMode(2, 0x2);
    pinMode(13, 0x1);

    Serial.begin(9600);
}

void loop()
{
    pastLight = analogRead(A0);
    currentLight = pastLight;
    //Serial.println(pastLight);
    button = digitalRead(2);
    //Serial.println(button);
    digitalWrite(13, 0x1);
    //Serial.println(button);
    if(button){
        buttonTime = millis();
        //Serial.println("IN IF");
        while(pastLight + 50 > currentLight){
            lightTime = millis();
            currentLight = analogRead(A0);
            if((lightTime - buttonTime) > 5000){
                Serial.println("TIMEOUT");
                break;
            }
            //Serial.println(currentLight);
        }
        //Serial.println("#######");
        Serial.println(lightTime - buttonTime);
        digitalWrite(13, 0x0);
        delay(1000);
    }

}

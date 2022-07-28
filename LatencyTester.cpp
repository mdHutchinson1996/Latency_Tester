
int currentLight = 0;
int pastLight = 0;
int buttonTime = 0;
int lightTime = 0;
int button = 0;
void setup()
{
	pinMode(A0, INPUT);
    pinMode(2, INPUT_PULLUP);
    pinMode(LED_BUILTIN, OUTPUT);

    Serial.begin(9600);
}

void loop()
{
    pastLight = analogRead(A0);
    currentLight = pastLight;
    //Serial.println(pastLight);
    button = digitalRead(2);
    //Serial.println(button);
    digitalWrite(LED_BUILTIN, HIGH);
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
        digitalWrite(LED_BUILTIN, LOW);
        delay(1000);
    }
    
}

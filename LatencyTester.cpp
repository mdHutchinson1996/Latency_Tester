
//Initialize variables
int currentLight = 0;
int pastLight = 0;
int buttonTime = 0;
int lightTime = 0;
int button = 0;

void setup()
{
    //setup inputs.
	pinMode(A0, INPUT); //A0 is for the photosensor
    pinMode(2, INPUT_PULLUP); //pin 2 is for the button
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    // Read read the current light levels from the photosensor
    pastLight = analogRead(A0);
    currentLight = pastLight;
    // Read button input
    button = digitalRead(2);
    digitalWrite(LED_BUILTIN, HIGH);
    // if the button is pressed
    if(button){
        //count the time at button press
        buttonTime = millis();
        //loop until the current light is greater than the past light + 50 (The screen flashes)
        while(pastLight + 50 > currentLight){
            // collect the current time
            lightTime = millis();
            currentLight = analogRead(A0);
            // Simple timeout. If it takes more than 5 seconds for light to flash. break loop
            if((lightTime - buttonTime) > 5000){
                Serial.println("TIMEOUT");
                break;
            }
        }
        // Print the time it took for the light to come on subtract the time of the button press to get difference between button input and screen output.
        Serial.println(lightTime - buttonTime);  
        digitalWrite(LED_BUILTIN, LOW);
        // Wait 1 second to allow the screen to go back to black
        delay(1000);
    }
    
}

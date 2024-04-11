#include "FastLED.h"

FASTLED_USING_NAMESPACE

#if defined(FASTLED_VERSION) && (FASTLED_VERSION < 3001000)
#warning "Requires FastLED 3.1 or later; check github for latest code."
#endif

//#define FASTLED_FORCE_SOFTWARE_SPI
#define DEBUG_PIN   33

#define DATA_PIN    4
//#define CLK_PIN   13
#define LED_TYPE    WS2812
#define COLOR_ORDER GRB
#define NUM_LEDS    20
CRGB leds[NUM_LEDS];

#define BRIGHTNESS         31



uint8_t gHue = 0; // rotating "base color" used by many of the patterns

void setup() 
{
  delay(1000); // 3 second delay for recovery

  pinMode(DEBUG_PIN, OUTPUT);  //set debug pin as output
  Serial.begin(9600);
  
  // tell FastLED about the LED strip configuration
  //FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  //FastLED.addLeds<LED_TYPE,DATA_PIN,CLK_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  //FastLED.addLeds<APA102,11,13,RGB,DATA_RATE_MHZ(16)>(leds,NUM_LEDS);  //10
  // set master brightness control
  FastLED.addLeds<WS2812,DATA_PIN,COLOR_ORDER>(leds,NUM_LEDS);
  FastLED.setBrightness(BRIGHTNESS);

  int count = 0;
  const char* patternChars;    // Get the length of the pattern
  int patternLength;
  
}
  
void loop()
{
  //FastLED.clearData();

  //for (int i = 0; i < NUM_LEDS; i++)
  //{
    //  leds[i] = 0x0000;
    
  //}
  
  /*for (int i = 37; i < 39; i++){
    leds[i] = CRGB::Black;
  }*/
  int count = -1;
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show(); 
  while (1){
    
    if (Serial.available() > 0) {
      // Read the incoming data
      String receivedData = Serial.readString();
      if(receivedData == "next"){
        count = count +1;
        if(count != NUM_LEDS){
          fill_solid(leds, NUM_LEDS, CRGB::Black);
          leds[count] = CRGB::Green;
          FastLED.show();
        }
        else if(count == NUM_LEDS){
          String receivedData = Serial.readString();
          fill_solid(leds, NUM_LEDS, CRGB::Black);
          int patternLength = receivedData.length();
          leds[count] = CRGB::Green;
          for(int i =0; i < patternLength ; i++){
            if(receivedData.charAt(i) == '1'){
              leds[i] = CRGB::Green;
            }
          }
          FastLED.show();
          count = 0;
        }
      }
      else if(receivedData.charAt(0) == '0' || receivedData.charAt(0) == '1'){
        int patternLength = receivedData.length();
        fill_solid(leds, NUM_LEDS, CRGB::Black);
        for(int i =0; i < patternLength ; i++){
          if(receivedData.charAt(i) == '1'){
            leds[i] = CRGB::Green;
          }
        }
        FastLED.show();
      }
      
      
      
    }
  }

   // Update LED display
}



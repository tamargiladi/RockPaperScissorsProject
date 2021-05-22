/*************************************************** 
  This is an example for our Adafruit 16-channel PWM & Servo driver
  Servo test - this will drive 8 servos, one after the other on the
  first 8 pins of the PCA9685

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/products/815
  
  These drivers use I2C to communicate, 2 pins are required to  
  interface.

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);
// you can also call it with a different address and I2C interface
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40, Wire);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define SERVOMG996RMIN  100 // this is min value
#define SERVOMG996RMAX  480 // this is max value
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

//----------pulse length count for open/close------//
int val; // initial value of input
int thumbClose = 100;
int thumbOpen = 310;
int indexFingerClose = 100;
int indexFingerOpen = 320;
int middleFingerClose = 100;
int middleFingerOpen = 320;
int ringFingerOpen = 100;
int ringFingerClose = 300;
int pinkyFingerOpen = 110;
int pinkyFingerClose = 300;

//--------------delay time----------//
int shortDelayTime = 100;
int longDelayTime = 200;

//------------------servo number--------//
int thumbServo = 0;
int indexFingerServo = 1;
int middleFingerServo = 2;
int ringFingerServo = 3;
int pinkyFingerServo = 4;

bool thumb = true;
bool indexFinger = false;

void openMiddleFinger(){

  Serial.println("Middle Finger open");
  pwm.setPWM(middleFingerServo, 0, middleFingerOpen);
  delay(shortDelayTime);
}

void closeMiddleFinger(){

  Serial.println("Middle Finger close");
  pwm.setPWM(middleFingerServo, 0, middleFingerClose);
  delay(shortDelayTime);
}

void openRingFinger(){
  
  Serial.println ("Ring Finger open");
  pwm.setPWM(ringFingerServo, 0, ringFingerOpen);
  delay(shortDelayTime);
}

void closeRingFinger(){

  Serial.println("Ring Finger close");
  pwm.setPWM(ringFingerServo, 0, ringFingerClose);
  delay(shortDelayTime);  
}

void openPinkyFinger(){

  Serial.println("Pinky Finger open");
  pwm.setPWM(pinkyFingerServo, 0, pinkyFingerOpen);
  delay(shortDelayTime);
}

void closePinkyFinger(){
 
  Serial.println("Pinky Finger close");
  pwm.setPWM(pinkyFingerServo, 0, pinkyFingerClose);
  delay(shortDelayTime);
}

void openThumb(){

  Serial.println("Thumb open");
  pwm.setPWM(thumbServo, 0, thumbOpen);
  delay(shortDelayTime);
  thumb = false;
}

void closeThumb(){

  Serial.println("Thumb close");
  pwm.setPWM(thumbServo, 0, thumbClose);
  delay(shortDelayTime);
  thumb = true;
}

void openIndexFinger(){

   if (indexFinger == true){
      if (thumb==true) // open thumb first.
    {
      openThumb();
      pwm.setPWM(indexFingerServo, 0, indexFingerOpen);
      Serial.println("Index Finger open");
      delay(longDelayTime);
      closeThumb();
    }
    else{
       pwm.setPWM(indexFingerServo, 0, indexFingerOpen);
       Serial.println("Index Finger open");
       delay(shortDelayTime);
    }
    
    indexFinger = false;
   }
}


void closeIndexFinger(){
  
 if(indexFinger== false){
      if (thumb==true)
    {
      openThumb();
      pwm.setPWM(indexFingerServo, 0, indexFingerClose);
      Serial.println("Index Finger close");
      delay(longDelayTime);
      delay(shortDelayTime);
      closeThumb();
    }
    else
    {
     pwm.setPWM(indexFingerServo, 0, indexFingerClose);
     Serial.println("Index Finger close");
     delay(shortDelayTime);
    } 
    indexFinger = true;
 }
}

void openAll(){
  
    Serial.println("all open");
    if (thumb == true){
      openThumb();
    }
    thumb = false;
    openIndexFinger();
    indexFinger = false;
    openMiddleFinger();
    openRingFinger();
    openPinkyFinger();
}

void closeAll(){
  
    Serial.println("all close");
    if (indexFinger == false){
      closeIndexFinger();
    }
    indexFinger = true;
    
    closeMiddleFinger();
    closeRingFinger();
    closePinkyFinger();
     
    if (thumb == false){
      delay(shortDelayTime);
      closeThumb();
    }
    thumb = true;
}


void scissors(){

    Serial.println("Scissors");
    if (indexFinger == true){
      openIndexFinger();
    }
    openMiddleFinger();
    closeRingFinger();
    closePinkyFinger();
   
    if (thumb == false){
      closeThumb();
    }
    thumb = true;
    
}

void setup() {
  Serial.begin(9600);
  Serial.println("Hand Ready!");
  pwm.begin();
  /*
   * In theory the internal oscillator (clock) is 25MHz but it really isn't
   * that precise. You can 'calibrate' this by tweaking this number until
   * you get the PWM update frequency you're expecting!
   * The int.osc. for the PCA9685 chip is a range between about 23-27MHz and
   * is used for calculating things like writeMicroseconds()
   * Analog servos run at ~50 Hz updates, It is importaint to use an
   * oscilloscope in setting the int.osc frequency for the I2C PCA9685 chip.
   * 1) Attach the oscilloscope to one of the PWM signal pins and ground on
   *    the I2C PCA9685 chip you are setting the value for.
   * 2) Adjust setOscillatorFrequency() until the PWM update frequency is the
   *    expected value (50Hz for most ESCs)
   * Setting the value here is specific to each individual I2C PCA9685 chip and
   * affects the calculations for the PWM update frequency. 
   * Failure to correctly set the int.osc value will cause unexpected PWM results
   */
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates

  delay(10);
  closeAll();
}

// You can use this function if you'd like to set the pulse length in seconds
// e.g. setServoPulse(0, 0.001) is a ~1 millisecond pulse width. It's not precise!
void setServoPulse(uint8_t n, double pulse) {
  double pulselength;
  
  pulselength = 1000000;   // 1,000,000 us per second
  pulselength /= SERVO_FREQ;   // Analog servos run at ~60 Hz updates
  Serial.print(pulselength); Serial.println(" us per period"); 
  pulselength /= 4096;  // 12 bits of resolution
  Serial.print(pulselength); Serial.println(" us per bit"); 
  pulse *= 1000000;  // convert input seconds to us
  pulse /= pulselength;
  Serial.println(pulse);
  pwm.setPWM(n, 0, pulse);
}



void loop() {
 
 if (Serial.available()) // if serial value is available
 {
  val = Serial.read();// then read the serial value
  
  if (val == '1') //if value input is equals to d
  {
    closeThumb();
  }
  
  
  if (val == '2') //if value input is equals to a
  {
    openThumb();
  }
  
  
  if (val == '3') //if value input is equals to d
  {
    closeIndexFinger();
  }
  
  
  if (val == '4') //if value input is equals to a
  {
    openIndexFinger();
  }
  
    
  if (val == '5') //if value input is equals to d
  {
    closeMiddleFinger();
  }
  
  
  if (val == '6') //if value input is equals to a
  {
    openMiddleFinger();
  }
  
  
  if (val == '8') //if value input is equals to d
  {
    openRingFinger();
  }
  
  
  if (val == '7') //if value input is equals to a
  {
    closeRingFinger();
  }
  

    if (val == '0') //if value input is equals to d
  {
    openPinkyFinger();
  }
  
  
  if (val == '9') //if value input is equals to a
  {
    closePinkyFinger();
  }
  

  if (val == 'o' || val == 'p') //if value input is equals to a
  {
    openAll();
  }
  

  if (val == 'c' || val == 'r') //if value input is equals to a
  {
    closeAll();
  }

  if (val == 's') //if value input is equals to a
  {
    scissors();
  }
  Serial.println("-----------------------");
  }
  
}

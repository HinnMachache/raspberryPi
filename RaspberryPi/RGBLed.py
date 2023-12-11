from machine import PWM,Pin
from time import sleep

redPin = 13
bluePin = 14
greenPin = 15
redLed = PWM(Pin(redPin, Pin.OUT))
blueLed = PWM(Pin(bluePin, Pin.OUT))
greenLed = PWM(Pin(greenPin, Pin.OUT))
redLed.freq(1000)
redLed.duty_u16(65535)
blueLed.freq(1000)
blueLed.duty_u16(65535)
greenLed.freq(1000)
greenLed.duty_u16(65535)


def userDefinedRGB():
    color = input('Input Desired Color: (Red) (Green) (Blue) (Magenta) (Cyan) (Yellow) (White) (Orange) ')
    color = color.lower()
    if color == 'red':
        redBrightness = 0
        greenBrightness = 65535
        blueBrightness = 65535
    if color == 'green':
        redBrightness = 65535
        greenBrightness = 0
        blueBrightness = 65535
    if color == 'blue':
        redBrightness = 65535
        greenBrightness = 65535
        blueBrightness = 0
    if color == 'magenta':
        redBrightness = 0
        greenBrightness = 65535
        blueBrightness = 0
    if color == 'cyan':
        redBrightness = 65535
        greenBrightness = 32768
        blueBrightness = 32768
    if color == 'yellow':
        redBrightness = 0
        greenBrightness = 0
        blueBrightness = 65535
    if color == 'white':
        redBrightness = 0
        greenBrightness = 0
        blueBrightness = 0
    if color == 'orange':
        redBrightness = 0
        greenBrightness = 42401
        blueBrightness = 65535
        
    redLed.duty_u16(redBrightness)
    greenLed.duty_u16(greenBrightness)
    blueLed.duty_u16(blueBrightness)
        
while True:
    
    userDefinedRGB()
             
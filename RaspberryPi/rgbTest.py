from machine import Pin

# Setting RGB
redPin = 13
bluePin = 14
greenPin = 15

redLed = Pin(redPin, Pin.OUT)
blueLed = Pin(bluePin, Pin.OUT)
greenLed = Pin(greenPin, Pin.OUT)

redLed.on()
greenLed.on()
blueLed.on()
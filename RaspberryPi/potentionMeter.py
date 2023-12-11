import machine
from time import sleep

redPin = 13
greenPin = 14
yellowPin = 15
redLed = machine.Pin(redPin, machine.Pin.OUT)
greenLed = machine.Pin(greenPin, machine.Pin.OUT)
yellowLed = machine.Pin(yellowPin, machine.Pin.OUT)
potPin = 28
myPotPin = machine.ADC(potPin)

    
def potLed(value):
    if (value >= 90 and value <= 100):
        redLed.on()
        greenLed.off()
        yellowLed.off()
    elif (value >= 70 and value <= 89):
        yellowLed.on()
        redLed.off()
        greenLed.off()
    else:
        greenLed.on()
        redLed.off()
        yellowLed.off()
        
        
while True:
    potVal = myPotPin.read_u16()
    # voltage = ((3.3 / 65263) * (potVal - 3.3))
    value = ((100 / 65263) * (potVal - 272))
    print(value)
    potLed(value)
    sleep(.5)
    

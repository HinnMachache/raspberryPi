from machine import PWM, Pin
from time import sleep

analogPin = 15
LedPin = PWM(Pin(analogPin, Pin.OUT))
LedPin.freq(1000)
LedPin.duty_u16(0)

while True:
    myVoltage = float(input('Input Voltage to Supply to LED: '))
    if (myVoltage >= 3.3):
        myVoltage = 3.3
    if (myVoltage <= 0):
        myVoltage = 0
    LedVoltage = (65535 / 3.3) * myVoltage
    print(LedVoltage)
    LedPin.duty_u16(int(LedVoltage))
             
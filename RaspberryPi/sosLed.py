from machine import Pin
from time import sleep
ledPin = Pin(15, Pin.OUT)

def ledSos():
    ledPin.on()
    sleep(.1)
    ledPin.off()
    sleep(.1)
    
while True:
    ledSos()
    ledSos()
    ledSos()
    sleep(2)


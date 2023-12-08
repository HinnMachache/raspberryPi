from machine import Pin
from time import sleep
ledPin = Pin(15, Pin.OUT)
while True:
    led.toggle()
    sleep(.5)
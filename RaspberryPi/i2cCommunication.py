from machine import Pin, I2C
from time import sleep

sclPin = 17
sdaPin = 16
MSG_SIZE = 17
i2cPin = I2C(0, scl=Pin(sclPin), sda=Pin(sdaPin), freq = 10000)
addr = i2cPin.scan()[0]
# print(12cPin.scan())

#Send and Receive Data to Other Peripherl

i2cPin.writeto(addr, "Hi From Pico W")
sleep(0.1)
data = i2cPin.readfrom(addr, MSG_SIZE)
print(data)
print("Message Received:", data, "Address", addr)


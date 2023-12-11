import network
import socket
import time
import machine

# Setting RGB
redPin = 13
bluePin = 14
greenPin = 15
redLed = machine.Pin(redPin, machine.Pin.OUT)
blueLed = machine.Pin(bluePin, machine.Pin.OUT)
greenLed = machine.Pin(greenPin, machine.Pin.OUT)

redLed.on()
greenLed.on()
blueLed.on()

# Setting up Wifi
raspWifi = network.WLAN(network.STA_IF) # Creating wifi object
raspWifi.active(True) # Activate raspWifi Object
raspWifi.disconnect()
raspWifi.connect('Humphrey tech', 'humphrey7436') # Connect to Wifi

# Check for Wifi connectivity
max_wait = 10
while max_wait > 0:
    if (raspWifi.status() < 0 or raspWifi.status() >= 3):
        break
    max_wait -= 1
    print('Waiting For Connection . . .')
    time.sleep(1)

# Handle Wifi Connection Failure
if (raspWifi.status() != 3):
    raise RuntimeError('Network Connection Failed')
else:
    print('Wifi Connected Succesfully')

serverInfo = raspWifi.ifconfig()
serverIP = serverInfo[0]
serverPort = 2222 # Allows for interaction
bufferSize = 1024
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Allows for receiveing / Sending of data
UDPServer.bind((serverIP, serverPort)) # Connect to IP, Port
print('IP:', serverIP,'\nPort:', serverPort)
print('UDP Server Up and Waiting . . .')
# Listen to Commands

while True:
    command, address = UDPServer.recvfrom(bufferSize)
    cmdDecoded = command.decode('utf-8')
    print('Command Received:', cmdDecoded, '. From:', address[0])
    dataString = 'Received Your Command\n' +cmdDecoded + ' LED is On'
    dataEncoded = dataString.encode('utf-8')
    UDPServer.sendto(dataEncoded, address)
    color = cmdDecoded.lower()
    if color == 'red':
        redLed.off()
        greenLed.on()
        blueLed.on()
    if color == 'green':
        redLed.on()
        greenLed.off()
        blueLed.on()
    if color == 'blue':
        redLed.on()
        greenLed.on()
        blueLed.off()



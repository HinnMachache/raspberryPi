import network
import time
import socket

raspWifi = network.WLAN(network.STA_IF) # Create Wifi Object
raspWifi.active(True) # Activate Wifi Object
raspWifi.connect('Humphrey tech', 'humphrey7436') # Connect To Wifi

# Check for Wifi Connectivity Status
# Settting Connection TimeOut
max_wait = 10
while max_wait > 0:
    if raspWifi.status() < 0 or raspWifi.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for Connection . . .')
    time.sleep(1)

# Handle Connection Error
if raspWifi.status() != 3:
    raise RuntimeError('Network Connection Failed')
else:
    print('Connected')
    status = raspWifi.status()
    config = raspWifi.ifconfig()
    #print(status)
    print(' IP = ' + config[0])

ServerIP = config[0] # The Server / Raspberry IP address
ServerPort = 2222 # Port to allow for interaction within the applications
bufferSize = 1024 # Data Packet Size

# Creating a socket
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Allows for receiving / Sending of data
UDPServer.bind((ServerIP, ServerPort))    
print('UDP Server Up and Waiting . . .')

# Listening for a command
while (True):
    message, address = UDPServer.recvfrom(bufferSize) # Receive the client data
    messageDecoded = message.decode('utf-8')
    print('Message Received:',messageDecoded, '. From:', address[0])
    dataString = 'Received Your Command ' +messageDecoded + '.'
    dataStringEncoded = dataString.encode('utf-8')
    UDPServer.sendto(dataStringEncoded, address)

# print(raspWifi.ifconfig())


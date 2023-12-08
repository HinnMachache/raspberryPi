import network
import time
import socket

wifi = network.WLAN(network.STA_IF) # Creating wifi Object
wifi.active(True)

# wifi.disconnect()
wifi.connect('Humphrey tech', 'humphrey7436')

while wifi.isconnected() == False:
    print('Waiting for Connection . . .')
    time.sleep(1)
    
wifiInfo = wifi.ifconfig() # Get Server IP Address
print(wifiInfo)
ServerIP = wifiInfo[0]
ServerPort = 2222 # Socket Number
bufferSize = 1024 # Max Packet Size
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServer.bind((ServerIP, ServerPort))
print('UDP Server Up and waiting...')
while True:
    message, address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode('utf-8')
    print('Received Message:',messageDecoded, '. From:',address[0])
    dataString = 'Received Your Message:' +messageDecoded
    dataStringEncoded = dataString.encode('utf-8')
    UDPServer.sendto(dataStringEncoded, address)
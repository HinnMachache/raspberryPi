import socket
import time

serverAddress = ('192.168.100.27', 2222)
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    command = input('Input Desired Color: ')
    cmdEncoded = command.encode('utf-8')
    UDPClient.sendto(cmdEncoded, serverAddress)
    dataReceived,address = UDPClient.recvfrom(bufferSize)
    dataDecoded = dataReceived.decode('utf-8')
    print(dataDecoded)
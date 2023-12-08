import socket

serverAddress = ('192.168.100.27', 2222)
bufferSize = 1024

# Open a socket
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while (True):
    cmd = input("Input you Command: ")
    cmdEncoded = cmd.encode('utf-8')
    UDPClient.sendto(cmdEncoded, serverAddress)
    data, address = UDPClient.recvfrom(bufferSize)
    dataDecoded = data.decode('utf-8')
    print(dataDecoded, 'From' , address[0])
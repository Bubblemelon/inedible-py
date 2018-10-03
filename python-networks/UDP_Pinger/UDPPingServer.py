from socket import*

# this module is needed to generate randomized lost packets
import random

serverPort = 12000

# create a UDP socket
# SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# assign IP address and port number to socket
serverSocket.bind(('localhost' ,serverPort))

# at this point, server should be ready
print("\n The UDP Ping server is ready to receive!")

while True:

    # generate a random number from the range 0 to 10
    rand = random.randint(0,10);

    # receive the client packet along with its address (from which it came)
    # 1024 bytes is the amount of data to be received at once (buffer size)
    #
    # https://stackoverflow.com/questions/36115971/recv-and-recvfrom-socket-programming-using-python
    message, clientAddress = serverSocket.recvfrom(1024)

    # capitalize the message from the client
    modifiedMessage = message.decode().upper()

    #
    # If rand is less than 4 , then consider a packet at this time as lost
    # so don't respond. Otherwise continue/respond.
    #
    if rand < 4:
        continue
    # respond by sending the capitalize message back to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

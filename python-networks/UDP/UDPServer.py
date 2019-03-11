from socket import*
import sys

serverPort = 12000

# create a UDP socket
# SOCK_DGRAM for UDP packets

serverSocket = socket(AF_INET, SOCK_DGRAM)

# assign IP address and port number to socket
serverSocket.bind(('localhost' ,serverPort))

# at this point, server should be ready
print("[status] UDP server is ready to receive.")

while True:

    # receive the client packet along with its address (from which it came)
    #
    # recvfrom returns a string in bytes and the address
    #
    # recv returns only the message string in bytes
    #
    # https://docs.python.org/3/library/socket.html#socket.socket.recv
    try:
        message, clientAddress = serverSocket.recvfrom(2048)

        print("[status] message received: " + message.decode() )

        # capitalize the message from the client
        modifiedMessage = message.decode().upper()

        # respond by sending the capitalize message back to the client
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    except KeyboardInterrupt:
        # captures ^C
                
        print("\n[status] UDP server is terminated.")
        sys.exit()

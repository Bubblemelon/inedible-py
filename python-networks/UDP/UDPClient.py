from socket import*

# server side address and port number
serverName = "localhost"
serverPort = 12000

# create a UDP socket
# SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# for python2
# message = raw_input('Input lowercase sentence:')

# for python3
message = input('Input lowercase sentence: ')

# send the encoded message to the UDP server using its IP address and Port number
clientSocket.sendto(message.encode(),( serverName, serverPort))

# automatically binds to a system-assigned local port number
# https://stackoverflow.com/questions/6189831/whats-the-purpose-of-using-sendto-recvfrom-instead-of-connect-send-recv-with-ud
#
# reads the server reply characters from socket into string
# receives message buffer size of 2048 bytes
modMsg, serverAddress = clientSocket.recvfrom(2048)

print (modMsg.decode())

# when complete close the socket connection
clientSocket.close()

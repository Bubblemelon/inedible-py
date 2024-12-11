from socket import*
import sys
import time
from datetime import datetime
import array
# datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# time.strftime(%H:%M:%S)

# needs two command line arguments
if len(sys.argv) < 2:
    print ('\nUsage:python3 UDPPingClient "message to server in lowercase" <Optional:Number of Pings>\n')
    sys.exit()

pingNum = 10

if len(sys.argv) == 3:
    print ("\nThis UDP Client will ping your message ("+ str(sys.argv[1]) +") " + str(sys.argv[2]) + " time(s) to the server.\n")
    pingNum = int(sys.argv[2])
else:
    print ("\nThis UDP Client will ping your message ("+ str(sys.argv[1]) +") 10 times to the server.\n")

# server side address and port number
# or 127.0.0.1
serverName = "localhost"
serverPort = 12000

# create a UDP socket
# SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# let the client wait up to 1 second for a reply
# if parameter is zero `0` then socket is put in non-blocking mode
# if parameter is `None`, then socket is put in blocking mode
# https://docs.python.org/3/library/socket.html#socket.socket.settimeout
clientSocket.settimeout(1)

# 10 pings

# declare rtt List
rttList = list()
# counter for received number
recvNum = 0

for x in range(pingNum):

    # time at which message was sent
    # for entire(whole) time in seconds = time.time()
    sT = time.time()
    #
    # this is for microseconds
    # sendTime = int(datetime.now().strftime("%f"))
    #
    # for time in miliseconds = int(round(time.time() * 1000))
    # micro to milli is divide by 1000
    # sendTime = sendTime/1000
    #
    # message = str(datetime.now().strftime("%M:%S")) + "." + str(sendTime) + " " + str(sys.argv[1])
    message = str(sys.argv[1])

    # send the encoded message to the UDP server using its IP address and Port number
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    try:
        modMsg, serverAddress = clientSocket.recvfrom(2048)

        # time at which message was received
        rT = time.time()
        #
        # in Microseconds
        # receiveTime = int(datetime.now().strftime("%f"))
        #
        # in Miliseconds
        # receiveTime = receiveTime/1000

        # Round Trip time (rtt): time for client -> server -> client
        # for microseconds
        # rtt = receiveTime - sendTime

        # seconds to miliseconds
        rtt = (rT - sT)*1000

        print ("Ping seq=" + str(x+1) + " message=" + modMsg.decode() + " time=%5.3fms\n" % rtt)

        # IGONORE If using print()s to mimic GNU ping Util:
        #
        # Time is in Minutes:Seconds.Milliseconds
        # print ("Time received: " + str(datetime.now().strftime("%M:%S")) + "." + str(receiveTime) )
        # print ("Round Trip Time: " + str(rtt) + " in mirco second")
        # print ("Round Trip Time: %6.2f ms\n" % rtt)

        rttList.append(rtt)

        recvNum += 1

    # settimeout() == will raise a timeout exception if the timeout period value
    # has elapsed before the operation has completed
    #
    except Exception as e:
        print ("Request timed out\n")
        # 1 second == 1000 miliseconds


# without "100 -" is the percentageReceived
percentageLost = (100 - ((recvNum/10)*100) )

print("--- "+ serverName +" ping statistics ---")

# time in this print statement is the total time elapsed
print(str(pingNum) + " packet(s) transmitted, %d received, %d%% packet loss, time %7.2fms" % ( recvNum, percentageLost, (sum(rttList) + (1000*(10-recvNum))) ) )

if not rttList:
    print("rtt min/avg/max = INFINTE/INFINTE/INFINTE ms\n")
else:
    # prints the min avg max Round Trip Time (rtt)
    print("rtt min/avg/max = %5.3f/%5.3f/%5.3f ms\n" % ( min(rttList), (sum(rttList)/len(rttList)) ,max(rttList) ) )

# when complete close the socket connection
clientSocket.close()

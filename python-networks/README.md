# python-networks

Network programming in Python.

## Content

<!-- ### [LegacyRouter](python-networks/LegacyRouter)

### [TCP](python-networks/TCP)

#### [Client_Chat](python-networks/TCP/Client_Chat)

### [Find_Connection_Order](python-networks/TCP/Find_First_Client) -->

### [UDP](python-networks/UDP)
A simple UDP Client and Server program. Execute the Client program to send a string message to the UDP Sever. The string message is then sent back to the Client in capitalized form (all uppercase characters) and then the Client program terminates.

See [demo](python-networks/UDP).

### [UDP_Pinger](python-networks/UDP_Pinger)
A Client program that pings the UDP Server program with a given message string,
and an optional number of pings. Completes the number of pings by ending with
`ping` statistics similar to `iputil`.

An extended functionality of UDP Client and Server from the [UDP](python-networks/UDP) directory.

See [demo](/python-networks/UDP_Pinger).

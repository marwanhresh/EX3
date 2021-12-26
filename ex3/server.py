 # import socket module
from socket import *
import sys  # In order to terminate the program



#Here, we have created a server socket and declared a host and port.
serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    # Fill in start
    # Fill in end
serverSocket.bind(('',6789))# this binds the port
serverSocket.listen(1)

# onto the while loop. Basically, the while loop will make the server endlessly loop.
while True:
    # Establish the connection
    print('Ready to serve...')
    #add “serverSocket.accept()”, which simply makes the server accept the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        message =  connectionSocket.recv(1024).decode()# amount of data sent
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read()# outputs file



        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 ok".encode())# HTTP ok message
        # Fill in start
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        # Fill in end
        # Close client socket
        # Fill in start
        # Fill in end
        connectionSocket.send(" 404 Not Found".encode())# send meessage error
        connectionSocket.close()# close the connection

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

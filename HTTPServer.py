#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept() #Fill in end
    try:
        message = connectionSocket.recv(1024) #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()

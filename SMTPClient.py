from socket import * 
msg = '\r\n I love computer networks!\r\n'
endmsg = '\r\n.\r\n'
sender = '<sender@mosecure.local>\r\n'
recipient = '<recipient@mosecure.local>\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = 'smtp.mosecure.local' #Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
serverName = 'smtp.mosecure.local'
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
	
# Send MAIL FROM command and print server response.

# Fill in start
fromCommand = 'MAIL FROM: ' + sender
clientSocket.send(fromCommand)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcptCommand = 'RCPT TO: ' + recipient
clientSocket.send(rcptCommand)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send DATA command and print server response.

# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
	print '354 reply not received from server.'
# Fill in end

# Send message data.

# Fill in start
clientSocket.send(msg)
# Fill in end

# Message ends with a single period.

# Fill in start
clientSocket.send(endmsg)
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send QUIT command and get server response.

# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand)
recv7 = clientSocket.recv(1024)
print recv7
if recv7[:3] != '221':
	print '221 reply not received from server.'
# Fill in end

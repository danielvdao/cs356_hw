from socket import socket, AF_INET, SOCK_STREAM
from struct import pack, unpack
from random import randint

serverPort = [35601, 35602, 35603]
serverIP = '128.83.144.56'

# creating a client socket 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort[0]))

# grab the ip address and port # that is arbitrarily selected
ip_addr = clientSocket.getsockname()[0]
port = clientSocket.getsockname()[1]


# building socket for the second communication
host = ip_addr
psock = socket(AF_INET, SOCK_STREAM)

# just take the port used for the client and add 1 to it
psock.bind((host, 0))
psock.listen(1)
# generating metadata
username = 'D.V.Dao\n'
server_specifier = serverIP + '-' + str(serverPort[0])
rand_num = randint(0, 9000)
user_num = str(rand_num)

# client specifier returns to where psock is located
client_specifier = psock.getsockname()[0]+ '-' + str(psock.getsockname()[1]) 
msg = 'ex1' + ' ' + server_specifier + ' ' + client_specifier + ' ' + user_num + ' ' + username

clientSocket.send(msg)

recv_arr = []

# receives the messages from the server 
recv_msg = clientSocket.recv(1024)
recv_arr.append(recv_msg)

recv_msg = clientSocket.recv(1024)
recv_arr.append(recv_msg)

# error handling to check for OK 
if recv_arr[1].split()[0] != 'OK':
    print 'OK MESSAGE NOT RECEIVED'
    sys.exit(1)

# printing the message and removing the \n character 
print msg[:-1]
print ''.join(recv_arr)[:-1]

# parsing for the server number and the client number, like exercise 0 
response_parse = recv_arr[1].split()
server_num = int(response_parse[3])
client_num = int(response_parse[1])

#psock accepting connections now 
newsock, addr = psock.accept()

# read in the message from the cs356 server 
cs_server_response = newsock.recv(1024).split()

# parsed for int 
new_value =  int(cs_server_response[-1])

print 'CS 356 server sent ' + str(new_value)
new_msg = str(server_num + 1) + ' ' + str(new_value + 1) + '\n'

# sent the message including the new random number 
newsock.send(new_msg) 

# closing the sockets 
newsock.close()
psock.close()

# receiving the last message from the client socket 
print clientSocket.recv(1024)

# closing the client socket 
clientSocket.close()


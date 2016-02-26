from socket import socket, AF_INET, SOCK_STREAM
from struct import pack, unpack
from random import randint 

# host port and IP 
serverPort = [35601, 35602, 35603]
serverIP = '128.83.144.56'


# creating the client socket 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort[0]))

# grabbing the ip address and port # that is arbitrarily selected
ip_addr = clientSocket.getsockname()[0]
port = clientSocket.getsockname()[1]

# building data for the first request
rand_num = randint(0, 9000)
server_specifier = serverIP + '-' + str(serverPort[0])
client_specifier = ip_addr + '-' + str(port)
user_num = str(rand_num)
username = 'D.V.Dao\n'
msg = 'ex0'+ ' ' + server_specifier + ' ' + client_specifier + ' ' + user_num + ' ' + username
clientSocket.send(msg)

recv_arr = []

# receives the messages from the server
recv_msg = clientSocket.recv(1024) 
recv_arr.append(recv_msg)

recv_msg = clientSocket.recv(1024) 
recv_arr.append(recv_msg)

# strip \n character
print msg[:-1]
print ''.join(recv_arr)[:-1]

# parsing for the number in the response
response_parse = recv_arr[1].split()
server_num = int(response_parse[3])
client_num = int(response_parse[1])

ack_string = 'ex0' + ' ' + str(client_num) + ' ' + str(server_num + 1) + '\n'

# sending ack string made above
clientSocket.send(ack_string)
recv_msg = clientSocket.recv(1024)

# strip \n character
print ack_string[:-1]
print recv_msg[:-1]
print int(recv_msg[:-1].split()[-1]) + 1
clientSocket.close()

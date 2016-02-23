from socket import * # required for socket calls
from struct import * # required for packing and unpacking

serverPort = 5000

#SOCK_STREAM is for TCP socket
#AF_INET is a family of protocols
serverSocket = socket(AF_INET, SOCK_STREAM) 

# 127.0.0.1 is our localhost address 
host = '127.0.0.1'

serverSocket.bind((host, serverPort))

#input to listen argument is an intenger
#the integer tells us how many connections can be waiting on this socket
serverSocket.listen(1)

print 'The server is ready to receive'

while 1:
    # addr contains the address of the client
    # addr is the IP and the port 
    connectionSocket, addr = serverSocket.accept()
    print 'Client address: ', addr

    # 1024 is the buffer size
    recv_sentence = connectionSocket.recv(1024)

    # i want the integer 
    recv_split = recv_sentence.split()
    #number = int(recv_split[-1])
    
    number = unpack('!L', recv_sentence)[0] 
    print 'Client sent message: ' + str(number)
    send_sentence = 'Hi Client, your number with 1 added is ' + str(number)

    # if i want to communicate with client, i want to use the connection socket
    connectionSocket.send(send_sentence)
    connectionSocket.close()


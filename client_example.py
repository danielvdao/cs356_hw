from socket import *
from struct import *
import random
import sys

serverPort = 5000
host = '127.0.0.1'
clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect((host, serverPort))

#number = sys.argv[1]
send_sentence = 'Hi this is client, sending you number: ' + str((random.randint(0,9000))) + '\n'
send_sentence += 'test \n'
#send_sentence = pack('!L', 123456)
clientsock.send(send_sentence)

recv_sentence = clientsock.recv(1024)
print 'Message from server: ' + recv_sentence
clientsock.close()

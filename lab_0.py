from socket import *
from struct import *
import sys

# host port and IP 
serverPort = [35601, 35062, 35603]
serverIP = '128.83.144.56'


# creating the client socket 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort[0]))

ip_addr = clientSocket.getsockname()[0]
port = clientSocket.getsockname()[1]


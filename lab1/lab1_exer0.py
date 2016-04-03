from socket import socket, SOCK_DGRAM, AF_INET
from struct import pack, unpack
from array import array
from random import randint
import binascii

serverPort = [35604, 35605, 35606]
serverIP = '128.83.144.56'

# creating client socket 
clientSocket = socket(AF_INET, SOCK_DGRAM)

# creating message deatils
header = 23331079
cookie = 21
request_data = 111111111
checksum = 0
msg = array('l')

msg.append(header)
msg.append(cookie)
msg.append(request_data)


def splitNum(num): 
    higherB = num >> 16 
    lowerB = num - (higherB << 16) 
    return higherB, lowerB

def computeChecksum(


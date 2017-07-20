#!/usr/bin/env python

import socket
import ssl
import sys


TCP_IP = '127.0.0.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
sslSocket = socket.ssl(s)
while 1:
    send = ''
    send = raw_input("What to send: ") + '\n' 
    if send == "\n": sys.exit()
    sslSocket.write(send)
    response = sslSocket.read(65535)
    print response  
s.close()

#print "received data:", response

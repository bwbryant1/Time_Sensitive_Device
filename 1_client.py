#!/usr/bin/env python

import socket
import ssl
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
ss = socket.ssl(s)
print ss.read(52-15)
while 1:
    send = ''
    send = raw_input("What to send: ") + '\n' 
    if send == "\n": sys.exit()
    ss.write(send)
    response = ss.read(65535)
    print response  
s.close()

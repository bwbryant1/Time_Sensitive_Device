'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
from hashlib import sha256 
from OpenSSL import SSL
 
HOST = ''  
PORT = 8887

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('key')
context.use_certificate_file('cert')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s = SSL.Connection(context, sock)
print 'Socket created'
 

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 

s.listen(10)
print 'Socket now listening'
 

def clientthread(conn):

    while True:
         
	try:
            data = conn.recv(65535)

	
        reply = data
        if data == "bowser:8e10e081fb25ecd15fcfe6c5960bbd2c9c8b9d66cce74f64230c8ee686a4dfbf":
	    conn.sendall("authenticated")
	else:
	    conn.sendall("authentication failed")
        if not data: 
            break
     
        #conn.sendall(reply)
     

    conn.close()
 

while 1:
    
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    
    start_new_thread(clientthread ,(conn,))
 
s.close()

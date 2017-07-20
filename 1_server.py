'''
    Simple socket server using threads
'''
 
import socket
import sys
from executables import *
from thread import *
from hashlib import sha256 
from OpenSSL import SSL
import pickle,json

"""
MySQL bits
"""
con = make_sql()
"""
End MySQL
"""
from executables import *
 
HOST = '0.0.0.0'  
PORT = 8888

BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

funcs = make_dict()
a = funcs[0]
b = funcs[1]



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

    conn.send("You have connected to the Bomb Server")  # echo
    while True:

        data = ''
        try:
            data = conn.recv(BUFFER_SIZE)
        except:
           print 'disconnected with ' + addr[0] + ':' + str(addr[1])
        if not data: break
        data = data.rstrip("\n")

        
        
        if data in a.keys():
            a[data](con)
            conn.send("I ran command: "+data)  # echo
            print b,str(conn.getpeername())
            
        elif data in b.keys():
            msg = ""
            msg = b[data](con,msg)
            del b[data]            
            print b , str(conn.getpeername())
            conn.send(str(conn.getpeername()) + " ran command: "+data+ " " + msg)  # echo
        else:
            conn.send("No Command ran")  # echo

    conn.close()
    
 

 

while 1:
    
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    
    start_new_thread(clientthread ,(conn,))
 
s.close()

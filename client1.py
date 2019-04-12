import socket
import sys
import time

s=socket.socket()
host=input(str("enter host name:"))
print("server will start host:",host)
port=8080
s.connect((host,port))
print("server waiting for message") 
while 1:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    print("server:",incoming_message)
    
    message=input(str(">>Client :"))
    message=message.encode()
    s.send(message)
    print("sent")
    print("")
                        

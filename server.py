import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("server will start host",host)
port=8080
s.bind((host,port))
print("server waiing for message")
s.listen(1)
conn,addr=s.accept()
print(addr,"connected")
while 1:
    message=input(str(">>  Server :"))
    message=message.encode() 
    conn.send(message)
    
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print("client",incoming_message)
    print("")
                        

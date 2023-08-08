import socket
import time

s = socket.socket()   #creat a  socket  object
host = socket.gethostname  #get  local host name
port = 13200
s.bind(host,port)   #bind port

s.listen(5)

while True:


    c,addr = s.accept() #establising client connections
    c.send('hello'.encode("utf-8"))
    print(c.recv(1024))
    time.sleep(1)
    c.close()
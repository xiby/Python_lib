from socket import *

HOST='localhost'
PORT=22354
BUFSIZE=1024
ADDR=(HOST,PORT)

sc=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input('>')
    if not data:
        break
    data=data.encode('utf-8')
    sc.sendto(data,ADDR)
    msg,addr=sc.recvfrom(BUFSIZE)
    print(msg.decode('utf-8'))
sc.close()
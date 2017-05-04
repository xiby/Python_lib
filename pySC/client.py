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
    if data=='2':
        data=data.encode('utf-8')
        sc.sendto(data,ADDR)
        msg,addr=sc.recvfrom(BUFSIZE)
        msg=msg.decode('utf-8')
        books=list()
        msg=msg.split(',')
        for item in msg:
            if len(item)==0:
                continue
            item =item.split(" ")
            books.append(item)
        print(books)
    else:
        data=data.encode('utf-8')
        sc.sendto(data,ADDR)
        msg,addr=sc.recvfrom(BUFSIZE)
        print(msg.decode('utf-8'))
sc.close()
from socket import *
from time import ctime

HOST=''
PORT=22354
BUFSIZE=1024
ADDR=(HOST,PORT)

sc=socket(AF_INET,SOCK_DGRAM)
sc.bind(ADDR)

dirct={'1':'insert','2':'serch','3':'delete'}
while True:
    print('waiting for massage...')
    while True:
        data,addr=sc.recvfrom(BUFSIZE)
        if not data:
            break
        data=data.decode('utf-8')
        data=data.split(' ')
        msg=''
        flag=True
        if data[0]=='1':
            data[0]=dirct.get('1')
        elif data[0]=='2':
            data[0]=dirct.get('2')
        elif data[0]=='3':
            data[0]=dirct.get('3')
        else:
            flag=False
        if flag:
            for m in data:
                msg=msg+m+' '
        else:
            msg='invalid instruction!'
        print(msg)
        msg=msg.encode('utf-8')
        sc.sendto(msg,addr)
sc.close()
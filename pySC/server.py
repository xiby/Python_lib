from socket import *
import time
import dataBase

HOST=''
PORT=22354
BUFSIZE=1024
ADDR=(HOST,PORT)

myLib=dataBase.libdb()

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
        if data[0]=='1':                #表明此时要插入数据
            book=list()
            book.append(data[1])
            book.append(data[2])
            now=time.strftime("%Y %m %d %X",time.localtime())
            now=now.split(" ")
            book.append(now[0])
            book.append(now[1])
            book.append(now[2])
            
            book.append(1)
            print(book)
            myLib.insert(book)
        elif data[0]=='2':              #表明此时要查询全部数据
            print(myLib.search())
            data[0]=dirct.get('2')
        elif data[0]=='3':              #表明此时要删除数据
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
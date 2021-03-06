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

dirct={'1':'insert','2':'serch','3':'delete','4':'search on name','5':'search on publicher','6':'search on date'}
while True:
    print('waiting for massage...')
    while True:
        data,addr=sc.recvfrom(BUFSIZE)
        if not data:
            break
        data=data.decode('utf-8')
        data=data.split(' ')
        msg=''
        m=''
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
            # print(book)
            m=myLib.insert(book)
        elif data[0]=='2':              #表明此时要查询全部数据
            m=(myLib.search())
            print(m)
            inf=''
            for item in m:
                for ditel in item:
                    inf=inf+str(ditel)+' '
                inf=inf.strip()
                inf=inf+','
            print(inf)
            m=inf
        elif data[0]=='3':              #表明此时要删除数据
            data[0]=dirct.get('3')
        elif data[0]=='4':              #按照书名查询
            name=data[1]
            m=myLib.searchByName(name)
            inf=''
            for item in m:
                for ditel in item:
                    inf=inf+str(ditel)+' '
                inf=inf.strip()
                inf=inf+','
            print(inf)
            m=inf
        elif data[0]=='5':              #按照出版社查询
            pub=data[1]
            m=myLib.searchByPub(pub)
            inf=''
            for item in m:
                for ditel in item:
                    inf=inf+str(ditel)+' '
                inf=inf.strip()
                inf=inf+','
            print(inf)
            m=inf
        elif data[0]=='6':              #查询正在阅读的书目
            m=myLib.search_reading()
            inf=""
            for item in m:
                for ditel in item:
                    inf=inf+str(ditel)+' '
                inf=inf.strip()
                inf=inf+','
            m=inf
            
        elif data[0]=='0':
            sc.close()
            break
        elif data[0]=='7':              #此时要更新数据
            book=list()
            book.append(data[1])
            book.append(data[2])
            m=myLib.finish(book)
        else:
            flag=False
        if flag:
            msg=msg+m
        else:
            msg='invalid instruction!'
        msg=msg.encode('utf-8')
        sc.sendto(msg,addr)
        
sc.close()
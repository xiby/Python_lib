from socket import *
import UI.tmpUI
import sys
from PyQt5.QtWidgets import QApplication,QWidget

HOST='localhost'
PORT=22354
BUFSIZE=1024
ADDR=(HOST,PORT)

sc=socket(AF_INET,SOCK_DGRAM)


app=QApplication(sys.argv)
w=QWidget()
ui=UI.tmpUI.Ui_Form()
msg='2'
msg=msg.encode('utf-8')
sc.sendto(msg,ADDR)
msg,addr=sc.recvfrom(BUFSIZE)
msg=msg.decode('utf-8')
books=list()
msg=msg.split(',')
for item in msg:
    if len(item)!=0:
        item=item.split(" ")
        books.append(item)
ui.setupUi(w,books)
w.show()
sys.exit(app.exec_())
sc.close()
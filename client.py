from socket import *
import UI.tmpUI
import UI.w_query_name
import UI.w_query_pub
import UI.w_addBook
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

def sendMSG(msg,sc):
    msg=msg.encode('utf-8')
    sc.sendto(msg,ADDR)

def getMSG(sc):
    msg,addr=sc.recvfrom(BUFSIZE)
    msg=msg.decode('utf-8')
    return msg

def finish(book):
    '''
    已经阅读完成某本书
    '''
    pass

def addBook(book):
    pass

def query_name(name):
    pass

def query_pub(pub):
    pass

def query_reading():
    pass

def query_history():
    pass

def getNew():
    pass




HOST='localhost'
PORT=22354
BUFSIZE=1024
ADDR=(HOST,PORT)

sc=socket(AF_INET,SOCK_DGRAM)


# app=QApplication(sys.argv)
# w=QWidget()
# ui=UI.tmpUI.Ui_Form()
# msg='2'
# sendMSG(msg,sc)
# msg=getMSG(sc)
# books=list()
# msg=msg.split(',')
# for item in msg:
#     if len(item)!=0:
#         item=item.split(" ")
#         books.append(item)
# ui.setupUi(w,books)
# w.show()
# sys.exit(app.exec_())
# sc.close()

class MainClass(QWidget):

    def query_name(self,name):
        self.Wchild=UI.w_query_name.Ui_w_query_name()
        self.Dialog=QtWidgets.QDialog(self)
        self.Wchild.setupUi(self.Dialog)
        self.Wchild.pushButtonOK.clicked.connect(self.APPClose)
        self.Wchild.pushButtonCancel.clicked.connect(self.APPClose)
        self.Wchild.pushButtonOK.clicked.connect(self.GetLine)
        self.Dialog.exec_()

    def query_pub(self,pub):
        self.Wchild=UI.w_query_pub.Ui_w_query_pub()
        self.Dialog=QtWidgets.QDialog(self)
        self.Wchild.setupUi(self.Dialog)
        self.Wchild.pushButtonCancel.clicked.connect(self.APPClose)
        self.Wchild.pushButtonOK.clicked.connect(self.GetLine_pub)
        self.Dialog.exec_()

    def addbook(self):
        self.Wchild=UI.w_addBook.Ui_w_addBook()
        self.Dialog=QtWidgets.QDialog(self)
        self.Wchild.setupUi(self.Dialog)
        self.Wchild.pushButtonCancel.clicked.connect(self.APPClose)
        self.Wchild.pushButtonOK.clicked.connect(self.GetLines_add)
        self.Wchild.pushButtonOK.clicked.connect(self.APPClose)
        self.Dialog.exec_()

    def finishbook(self):
        self.Wchild=UI.w_addBook.Ui_w_addBook()
        self.Dialog=QtWidgets.QDialog(self)
        self.Wchild.setupUi(self.Dialog)
        self.Wchild.pushButtonCancel.clicked.connect(self.APPClose)
        self.Wchild.pushButtonOK.clicked.connect(self.GetLines_finish)
        self.Wchild.pushButtonOK.clicked.connect(self.APPClose)
        self.Dialog.exec_()

    def APPClose(self):
        self.Dialog.close()

    def __init__(self,parent=None):
        super(MainClass,self).__init__(parent)
        self.ui=UI.tmpUI.Ui_Form()
        self.w=QWidget()
        msg='2'
        sendMSG(msg,sc)
        msg=getMSG(sc)
        books=list()
        msg=msg.split(',')
        for item in msg:
            if len(item)!=0:
                item=item.split(" ")
                books.append(item)
        self.ui.setupUi(self.w,books)
        self.ui.query_name.clicked.connect(self.query_name)
        self.ui.query_pub.clicked.connect(self.query_pub)
        self.ui.addBook.clicked.connect(self.addbook)
        self.ui.finish.clicked.connect(self.finishbook)
        self.ui.reading.clicked.connect(self.Get_reading)
        self.ui.history.clicked.connect(self.Get_history)

    def GetLine(self):
        LineData=self.Wchild.bookname.text()

    def GetLine_pub(self):
        msg='5 '
        LineData=self.Wchild.pubname.text()
        msg=msg+LineData
        sendMSG(msg,sc)
        msg=getMSG(sc)
        ans=getBook(msg)
        self.showAns(ans)

    def GetLines_add(self):
        msg='1 '
        msg=msg+self.Wchild.bookname.text()+' '+self.Wchild.pubname.text()
        sendMSG(msg,sc)
        msg=getMSG(sc)
        mBox=QtWidgets.QMessageBox(self)
        mBox.setText(msg)
        mBox.exec_()

    def GetLines_finish(self):
        msg='7 '
        msg=msg+self.Wchild.bookname.text()+' '+self.Wchild.pubname.text()
        sendMSG(msg,sc)
        msg=getMSG(sc)
        mBox=QtWidgets.QMessageBox(self)
        mBox.setText(msg)
        mBox.exec_()

    def Get_history(self):
        msg='2'
        sendMSG(msg,sc)
        msg=getMSG(sc)
        ans=list()
        msg=msg.split(",")
        for item in msg:
            ans.append(item.split(' '))
        self.showAns(ans)
  
    def Get_reading(self):
        msg='6'
        sendMSG(msg,sc)
        msg=getMSG(sc)
        ans=list()
        msg=msg.split(",")
        for item in msg:
            ans.append(item.split(' '))
        self.showAns(ans)

    def showAns(self,ans):
        self.clear()
        for i in range(len(ans)):
            for j in range(0,len(ans[i])):
                newItem=QtWidgets.QTableWidgetItem(str(ans[i][j]))
                self.ui.tableWidget.setItem(i,j,newItem)

    def clear(self):
        self.ui.tableWidget.clear()

    def getBook(self,msg):
        msg=msg.split(',')
        ans=list()
        for item in msg:
            ans.append(item.split(" "))
        return ans

if __name__=='__main__':
    app=QApplication(sys.argv)
    MainApp=MainClass()
    MainApp.w.show()
    sys.exit(app.exec_())
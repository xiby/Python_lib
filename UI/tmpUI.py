# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form,books):
        Form.setObjectName("Form")
        Form.resize(409, 278)
        Form.setStyleSheet("background-image: url(:/background.jpg);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 401, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        self.query_name = QtWidgets.QPushButton(Form)
        self.query_name.setGeometry(QtCore.QRect(10, 180, 75, 31))
        self.query_name.setObjectName("query_name")
        self.query_pub = QtWidgets.QPushButton(Form)
        self.query_pub.setGeometry(QtCore.QRect(110, 180, 75, 31))
        self.query_pub.setObjectName("query_pub")
        self.reading = QtWidgets.QPushButton(Form)
        self.reading.setGeometry(QtCore.QRect(220, 180, 75, 31))
        self.reading.setObjectName("reading")
        self.addBook = QtWidgets.QPushButton(Form)
        self.addBook.setGeometry(QtCore.QRect(320, 180, 75, 31))
        self.addBook.setObjectName("addBook")
        self.finish = QtWidgets.QPushButton(Form)
        self.finish.setGeometry(QtCore.QRect(60, 230, 75, 31))
        self.finish.setObjectName("finish")
        self.getNew = QtWidgets.QPushButton(Form)
        self.getNew.setGeometry(QtCore.QRect(270, 230, 75, 31))
        self.getNew.setObjectName("getNew")
        self.history = QtWidgets.QPushButton(Form)
        self.history.setGeometry(QtCore.QRect(170, 230, 75, 31))
        self.history.setObjectName("history")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        for i in range(0,len(books)):
            for j in range(0,len(books[i])):
                newItem=QtWidgets.QTableWidgetItem(str(books[i][j]))
                self.tableWidget.setItem(i,j,newItem)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PY_LIB"))
        self.query_name.setText(_translate("Form", "按书名查询"))
        self.query_pub.setText(_translate("Form", "按出版社查询"))
        self.reading.setText(_translate("Form", "当前正在阅读"))
        self.addBook.setText(_translate("Form", "增加图书"))
        self.finish.setText(_translate("Form", "阅读完成"))
        self.getNew.setText(_translate("Form", "获取推荐"))
        self.history.setText(_translate("Form", "历史记录"))

import UI.myResource_rc

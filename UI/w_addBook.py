# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_addBook.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_w_addBook(object):
    def setupUi(self, w_addBook):
        w_addBook.setObjectName("w_addBook")
        w_addBook.resize(342, 200)
        self.label = QtWidgets.QLabel(w_addBook)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(w_addBook)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.label_2.setObjectName("label_2")
        self.bookname = QtWidgets.QLineEdit(w_addBook)
        self.bookname.setGeometry(QtCore.QRect(130, 20, 121, 31))
        self.bookname.setObjectName("bookname")
        self.pubname = QtWidgets.QLineEdit(w_addBook)
        self.pubname.setGeometry(QtCore.QRect(130, 70, 121, 31))
        self.pubname.setObjectName("pubname")
        self.pushButtonOK = QtWidgets.QPushButton(w_addBook)
        self.pushButtonOK.setGeometry(QtCore.QRect(50, 150, 75, 23))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(w_addBook)
        self.pushButtonCancel.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(w_addBook)
        QtCore.QMetaObject.connectSlotsByName(w_addBook)

    def retranslateUi(self, w_addBook):
        _translate = QtCore.QCoreApplication.translate
        w_addBook.setWindowTitle(_translate("w_addBook", "Dialog"))
        self.label.setText(_translate("w_addBook", "       书名："))
        self.label_2.setText(_translate("w_addBook", "       出版社名："))
        self.pushButtonOK.setText(_translate("w_addBook", "ok"))
        self.pushButtonCancel.setText(_translate("w_addBook", "cancel"))


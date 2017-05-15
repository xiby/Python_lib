# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_query_name.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_w_query_name(object):
    def setupUi(self, w_query_name):
        w_query_name.setObjectName("w_query_name")
        w_query_name.resize(342, 138)
        self.label = QtWidgets.QLabel(w_query_name)
        self.label.setGeometry(QtCore.QRect(13, 40, 111, 21))
        self.label.setObjectName("label")
        self.bookname = QtWidgets.QLineEdit(w_query_name)
        self.bookname.setGeometry(QtCore.QRect(130, 30, 121, 31))
        self.bookname.setObjectName("bookname")
        self.pushButtonOK = QtWidgets.QPushButton(w_query_name)
        self.pushButtonOK.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(w_query_name)
        self.pushButtonCancel.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(w_query_name)
        QtCore.QMetaObject.connectSlotsByName(w_query_name)

    def retranslateUi(self, w_query_name):
        _translate = QtCore.QCoreApplication.translate
        w_query_name.setWindowTitle(_translate("w_query_name", "Dialog"))
        self.label.setText(_translate("w_query_name", "请输入要查询的书名："))
        self.pushButtonOK.setText(_translate("w_query_name", "ok"))
        self.pushButtonCancel.setText(_translate("w_query_name", "cancel"))


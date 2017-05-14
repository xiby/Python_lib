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
        for i in range(0,len(books)):
            for j in range(0,len(books[i])):
                newItem=QtWidgets.QTableWidgetItem(str(books[i][j]))
                self.tableWidget.setItem(i,j,newItem)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import UI.myResource_rc

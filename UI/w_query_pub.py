# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_query_pub.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_w_query_pub(object):
    def setupUi(self, w_query_pub):
        w_query_pub.setObjectName("w_query_pub")
        w_query_pub.resize(342, 138)
        self.label = QtWidgets.QLabel(w_query_pub)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.label.setObjectName("label")
        self.pubname = QtWidgets.QLineEdit(w_query_pub)
        self.pubname.setGeometry(QtCore.QRect(130, 29, 121, 41))
        self.pubname.setObjectName("pubname")
        self.pushButtonOK = QtWidgets.QPushButton(w_query_pub)
        self.pushButtonOK.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(w_query_pub)
        self.pushButtonCancel.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(w_query_pub)
        QtCore.QMetaObject.connectSlotsByName(w_query_pub)

    def retranslateUi(self, w_query_pub):
        _translate = QtCore.QCoreApplication.translate
        w_query_pub.setWindowTitle(_translate("w_query_pub", "Dialog"))
        self.label.setText(_translate("w_query_pub", "要查询的出版社名："))
        self.pushButtonOK.setText(_translate("w_query_pub", "ok"))
        self.pushButtonCancel.setText(_translate("w_query_pub", "cancel"))


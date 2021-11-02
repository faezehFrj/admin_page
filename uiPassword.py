# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_passewKZsw.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,QRect)
from PySide2.QtWidgets import *


class Ui_MainWindowPassword(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 180)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color:rgb(67, 77, 90);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lable_show_enter = QLabel(self.centralwidget)
        self.lable_show_enter.setObjectName(u"lable_show_enter")
        self.lable_show_enter.setGeometry(QRect(130, 0, 181, 61))
        self.lable_show_enter.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_check_pass = QPushButton(self.centralwidget)
        self.pushButton_check_pass.setObjectName(u"pushButton_check_pass")
        self.pushButton_check_pass.setGeometry(QRect(90, 130, 93, 28))
        self.pushButton_check_pass.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.pushButton_cancel_pass = QPushButton(self.centralwidget)
        self.pushButton_cancel_pass.setObjectName(u"pushButton_cancel_pass")
        self.pushButton_cancel_pass.setGeometry(QRect(220, 130, 93, 28))
        self.pushButton_cancel_pass.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(120, 50, 161, 31))
        self.lineEdit_password.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid rgb(0, 173, 239);\n"
"border-radius: 10px;\n"
"background-color:rgb(67, 77, 90);\n"
"font-size: 18px;\n"
"color:rgb(255, 255, 255);\n"
"qproperty-alignment: AlignCenter}")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.label_alarm_pass = QLabel(self.centralwidget)
        self.label_alarm_pass.setObjectName(u"label_alarm_pass")
        self.label_alarm_pass.setGeometry(QRect(114, 100, 181, 20))
        self.label_alarm_pass.setStyleSheet(u"color: rgb(173, 87, 70);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lable_show_enter.setText(QCoreApplication.translate("MainWindow", u"enter your password", None))
        self.pushButton_check_pass.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.pushButton_cancel_pass.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.label_alarm_pass.setText("")
    # retranslateUi


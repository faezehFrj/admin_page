#############################################################################
## Form generated from reading UI file 'AlaermSavenITQfz.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,QRect)
from PySide2.QtWidgets import *


class Ui_MainWindow_alarm_save(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 180)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"\n"
"background-color:rgb(67, 77, 90);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelAlaemEployeeSave = QLabel(self.centralwidget)
        self.labelAlaemEployeeSave.setObjectName(u"labelAlaemEployeeSave")
        self.labelAlaemEployeeSave.setGeometry(QRect(120, 30, 181, 61))
        self.labelAlaemEployeeSave.setStyleSheet(u"color: rgb(0, 173, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_alarm_save = QPushButton(self.centralwidget)
        self.pushButton_alarm_save.setObjectName(u"pushButton_alarm_save")
        self.pushButton_alarm_save.setGeometry(QRect(150, 110, 93, 28))
        self.pushButton_alarm_save.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelAlaemEployeeSave.setText(QCoreApplication.translate("MainWindow", u"Employee saved", None))
        self.pushButton_alarm_save.setText(QCoreApplication.translate("MainWindow", u"ok", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_employeeRzYFce.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindowDeleteAlarm(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 180)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color:rgb(67, 77, 90);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lable_show_delete = QLabel(self.centralwidget)
        self.lable_show_delete.setObjectName(u"lable_show_delete")
        self.lable_show_delete.setGeometry(QRect(60, 20, 301, 71))
        self.lable_show_delete.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_okey_delete = QPushButton(self.centralwidget)
        self.pushButton_okey_delete.setObjectName(u"pushButton_okey_delete")
        self.pushButton_okey_delete.setGeometry(QRect(100, 120, 93, 28))
        self.pushButton_okey_delete.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.pushButton_cancel_delete = QPushButton(self.centralwidget)
        self.pushButton_cancel_delete.setObjectName(u"pushButton_cancel_delete")
        self.pushButton_cancel_delete.setGeometry(QRect(210, 120, 93, 28))
        self.pushButton_cancel_delete.setStyleSheet(u"\n"
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
        self.lable_show_delete.setText(QCoreApplication.translate("MainWindow", u"Do you want to delete this employee?", None))
        self.pushButton_okey_delete.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.pushButton_cancel_delete.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_exportVouElX.ui'
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


class Ui_MainCreateExport(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 315)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"\n"
"background-color:rgb(67, 77, 90);\n"
"}")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 70, 161, 31))
        self.comboBox.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 30, 141, 20))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_ok = QPushButton(self.centralwidget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(170, 230, 93, 28))
        self.pushButton_ok.setStyleSheet(u"\n"
"background-color:\n"
"qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(18, 166, 233, 0.6), stop:1 rgba(55, 160, 207, 0.294));\n"
"border-radius: 13px;\n"
"\n"
"")
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(280, 230, 93, 28))
        self.pushButton_close.setStyleSheet(u"\n"
"background-color:\n"
"qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(18, 166, 233, 0.6), stop:1 rgba(55, 160, 207, 0.294));\n"
"border-radius: 13px;\n"
"\n"
"")
        self.lable_result_export = QLabel(self.centralwidget)
        self.lable_result_export.setObjectName(u"lable_result_export")
        self.lable_result_export.setGeometry(QRect(190, 280, 161, 16))
        self.lable_result_export.setStyleSheet(u"color: rgb(240, 255, 171);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"choose your month", None))
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.lable_result_export.setText("")
    # retranslateUi


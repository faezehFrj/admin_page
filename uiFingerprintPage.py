# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_fingerprintWGeXnI.ui'
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

import resources

class Ui_MainWindowFingerprint(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 315)
        MainWindow.setMinimumSize(QSize(530, 315))
        MainWindow.setMaximumSize(QSize(530, 315))
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow{\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"\n"
"background-color:rgb(67, 77, 90);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_click = QPushButton(self.centralwidget)
        self.pushButton_click.setObjectName(u"pushButton_click")
        self.pushButton_click.setGeometry(QRect(490, 10, 26, 26))
        self.pushButton_click.setStyleSheet(u"\n"
" border-radius: 15px;\n"
"background-image: url(:/back.png);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 90, 201, 31))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_lavel = QLabel(self.frame_2)
        self.label_lavel.setObjectName(u"label_lavel")
        self.label_lavel.setGeometry(QRect(20, 10, 171, 16))
        self.label_lavel.setStyleSheet(u"color: rgb(129, 127, 137);")
        self.framelavel1 = QFrame(self.frame_2)
        self.framelavel1.setObjectName(u"framelavel1")
        self.framelavel1.setGeometry(QRect(10, 10, 2, 19))
        self.framelavel1.setStyleSheet(u"background-color: rgb(129, 127, 137);")
        self.framelavel1.setFrameShape(QFrame.StyledPanel)
        self.framelavel1.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 130, 201, 31))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_level2 = QLabel(self.frame_3)
        self.label_level2.setObjectName(u"label_level2")
        self.label_level2.setGeometry(QRect(20, 10, 171, 16))
        self.label_level2.setStyleSheet(u"color: rgb(129, 127, 137);")
        self.frame_level2 = QFrame(self.frame_3)
        self.frame_level2.setObjectName(u"frame_level2")
        self.frame_level2.setGeometry(QRect(10, 10, 2, 19))
        self.frame_level2.setStyleSheet(u"background-color: rgb(129, 127, 137);")
        self.frame_level2.setFrameShape(QFrame.StyledPanel)
        self.frame_level2.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 170, 201, 31))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_level3 = QLabel(self.frame_7)
        self.label_level3.setObjectName(u"label_level3")
        self.label_level3.setGeometry(QRect(20, 10, 191, 16))
        self.label_level3.setStyleSheet(u"color: rgb(129, 127, 137);")
        self.frame_level3 = QFrame(self.frame_7)
        self.frame_level3.setObjectName(u"frame_level3")
        self.frame_level3.setGeometry(QRect(10, 10, 2, 19))
        self.frame_level3.setStyleSheet(u"background-color: rgb(129, 127, 137);")
        self.frame_level3.setFrameShape(QFrame.StyledPanel)
        self.frame_level3.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(20, 210, 201, 31))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_level4 = QLabel(self.frame_9)
        self.label_level4.setObjectName(u"label_level4")
        self.label_level4.setGeometry(QRect(20, 10, 171, 16))
        self.label_level4.setStyleSheet(u"color: rgb(129, 127, 137);")
        self.frame_level4 = QFrame(self.frame_9)
        self.frame_level4.setObjectName(u"frame_level4")
        self.frame_level4.setGeometry(QRect(10, 10, 2, 19))
        self.frame_level4.setStyleSheet(u"background-color: rgb(129, 127, 137);")
        self.frame_level4.setFrameShape(QFrame.StyledPanel)
        self.frame_level4.setFrameShadow(QFrame.Raised)
        self.alarm = QLabel(self.centralwidget)
        self.alarm.setObjectName(u"alarm")
        self.alarm.setGeometry(QRect(50, 270, 231, 16))
        self.alarm.setStyleSheet(u"color:rgb(129, 127, 137)")
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(300, 60, 181, 225))
        self.frame_11.setStyleSheet(u"background-image: url(:/finger_max.png);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add new ", None))
        self.pushButton_click.setText("")
        self.label_lavel.setText(QCoreApplication.translate("MainWindow", u"put your finger on device", None))
        self.label_level2.setText(QCoreApplication.translate("MainWindow", u"remove your fingerprint", None))
        self.label_level3.setText(QCoreApplication.translate("MainWindow", u"put your finger on device agian", None))
        self.label_level4.setText(QCoreApplication.translate("MainWindow", u"store", None))
        self.alarm.setText(QCoreApplication.translate("MainWindow", u"alarm", None))
    # retranslateUi





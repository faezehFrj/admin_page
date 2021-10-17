# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_employeePzRVku.ui'
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

class Ui_MainWindowAdmin(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-image:url(:/adminpage_employee.png)\n"
"}")
        self.icon_dashboard = QLabel(self.centralwidget)
        self.icon_dashboard.setObjectName(u"icon_dashboard")
        self.icon_dashboard.setGeometry(QRect(20, 300, 21, 21))
        self.icon_dashboard.setStyleSheet(u"\n"
"background-image:url(:/icon_dashboard.png)")
        self.icon_setting = QLabel(self.centralwidget)
        self.icon_setting.setObjectName(u"icon_setting")
        self.icon_setting.setGeometry(QRect(20, 230, 21, 21))
        self.icon_setting.setStyleSheet(u"\n"
"background-image:url(:/icon_select_user.svg)")
        self.icon_dashboard_3 = QLabel(self.centralwidget)
        self.icon_dashboard_3.setObjectName(u"icon_dashboard_3")
        self.icon_dashboard_3.setGeometry(QRect(20, 370, 25, 25))
        self.icon_dashboard_3.setStyleSheet(u"\n"
"background-image:url(:/icon.svg)")
        self.pushButton_admin_employee = QPushButton(self.centralwidget)
        self.pushButton_admin_employee.setObjectName(u"pushButton_admin_employee")
        self.pushButton_admin_employee.setGeometry(QRect(40, 230, 151, 28))
        self.pushButton_admin_employee.setStyleSheet(u"border-radius: 30px;\n"
"color: rgb(0, 173, 239);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_Adashboard = QPushButton(self.centralwidget)
        self.pushButton_Adashboard.setObjectName(u"pushButton_Adashboard")
        self.pushButton_Adashboard.setGeometry(QRect(40, 300, 151, 28))
        self.pushButton_Adashboard.setStyleSheet(u"border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_Asetting = QPushButton(self.centralwidget)
        self.pushButton_Asetting.setObjectName(u"pushButton_Asetting")
        self.pushButton_Asetting.setGeometry(QRect(30, 370, 151, 28))
        self.pushButton_Asetting.setStyleSheet(u"border-radius: 30px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(240, 60, 461, 721))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 20, 118, 138))
        self.pushButton_5.setStyleSheet(u"\n"
"background-color:\n"
"qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(18, 166, 233, 0.6), stop:1 rgba(55, 160, 207, 0.294));\n"
"border-radius: 13px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/bi_plus-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(22, 22))
        self.frame_employee1 = QFrame(self.frame)
        self.frame_employee1.setObjectName(u"frame_employee1")
        self.frame_employee1.setGeometry(QRect(160, 20, 121, 151))
        self.frame_employee1.setFrameShape(QFrame.StyledPanel)
        self.frame_employee1.setFrameShadow(QFrame.Raised)
        self.employee1 = QPushButton(self.frame_employee1)
        self.employee1.setObjectName(u"employee1")
        self.employee1.setGeometry(QRect(0, 0, 118, 141))
        self.employee1.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")

        self.frame_employee2 = QFrame(self.frame)
        self.frame_employee2.setObjectName(u"frame_employee2")
        self.frame_employee2.setGeometry(QRect(310, 20, 131, 151))
        self.frame_employee2.setFrameShape(QFrame.StyledPanel)
        self.frame_employee2.setFrameShadow(QFrame.Raised)
        self.employee2 = QPushButton(self.frame_employee2)
        self.employee2.setObjectName(u"employee2")
        self.employee2.setGeometry(QRect(0, 0, 118, 141))
        self.employee2.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.frame_employee4 = QFrame(self.frame)
        self.frame_employee4.setObjectName(u"frame_employee4")
        self.frame_employee4.setGeometry(QRect(160, 200, 121, 151))
        self.frame_employee4.setFrameShape(QFrame.StyledPanel)
        self.frame_employee4.setFrameShadow(QFrame.Raised)
        self.employee4 = QPushButton(self.frame_employee4)
        self.employee4.setObjectName(u"employee4")
        self.employee4.setGeometry(QRect(0, 0, 118, 141))
        self.employee4.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.frame_employee5 = QFrame(self.frame)
        self.frame_employee5.setObjectName(u"frame_employee5")
        self.frame_employee5.setGeometry(QRect(310, 200, 121, 151))
        self.frame_employee5.setFrameShape(QFrame.StyledPanel)
        self.frame_employee5.setFrameShadow(QFrame.Raised)
        self.employee5 = QPushButton(self.frame_employee5)
        self.employee5.setObjectName(u"employee5")
        self.employee5.setGeometry(QRect(0, 0, 118, 141))
        self.employee5.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.frame_employee6 = QFrame(self.frame)
        self.frame_employee6.setObjectName(u"frame_employee6")
        self.frame_employee6.setGeometry(QRect(10, 380, 121, 151))
        self.frame_employee6.setFrameShape(QFrame.StyledPanel)
        self.frame_employee6.setFrameShadow(QFrame.Raised)
        self.employee6 = QPushButton(self.frame_employee6)
        self.employee6.setObjectName(u"employee6")
        self.employee6.setGeometry(QRect(0, 0, 118, 141))
        self.employee6.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.frame_employee7 = QFrame(self.frame)
        self.frame_employee7.setObjectName(u"frame_employee7")
        self.frame_employee7.setGeometry(QRect(160, 380, 121, 151))
        self.frame_employee7.setFrameShape(QFrame.StyledPanel)
        self.frame_employee7.setFrameShadow(QFrame.Raised)
        self.employee7 = QPushButton(self.frame_employee7)
        self.employee7.setObjectName(u"employee7")
        self.employee7.setGeometry(QRect(0, 0, 118, 141))
        self.employee7.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.frame_employee8 = QFrame(self.frame)
        self.frame_employee8.setObjectName(u"frame_employee8")
        self.frame_employee8.setGeometry(QRect(310, 380, 121, 151))
        self.frame_employee8.setFrameShape(QFrame.StyledPanel)
        self.frame_employee8.setFrameShadow(QFrame.Raised)
        self.employee8 = QPushButton(self.frame_employee8)
        self.employee8.setObjectName(u"employee8")
        self.employee8.setGeometry(QRect(0, 0, 118, 141))
        self.employee8.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.frame_employee3 = QFrame(self.frame)
        self.frame_employee3.setObjectName(u"frame_employee3")
        self.frame_employee3.setGeometry(QRect(10, 180, 131, 171))
        self.frame_employee3.setFrameShape(QFrame.StyledPanel)
        self.frame_employee3.setFrameShadow(QFrame.Raised)
        self.employee3 = QPushButton(self.frame_employee3)
        self.employee3.setObjectName(u"employee3")
        self.employee3.setGeometry(QRect(0, 20, 118, 141))
        self.employee3.setStyleSheet(u"background-color:\n"
                                     "qlineargradient(spread:pad, x1:0.487, y1:0, x2:0.516, y2:1, stop:0 rgba(42, 64, 74, 0.6), stop:1 rgba(42, 64, 74, 0.264));\n"
                                     "border-radius: 13px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")

        self.horizontalLayout.addWidget(self.frame)

        self.frame_features_one_employee = QFrame(self.centralwidget)
        self.frame_features_one_employee.setObjectName(u"frame_features_one_employee")
        self.frame_features_one_employee.setGeometry(QRect(720, 0, 561, 801))
        self.frame_features_one_employee.setFrameShape(QFrame.StyledPanel)
        self.frame_features_one_employee.setFrameShadow(QFrame.Raised)
        self.label_t_name = QLabel(self.frame_features_one_employee)
        self.label_t_name.setObjectName(u"label_t_name")
        self.label_t_name.setGeometry(QRect(20, 10, 71, 21))
        self.label_t_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2 = QLabel(self.frame_features_one_employee)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 10, 71, 21))
        self.label_2.setStyleSheet(u"color: rgb(0, 173, 239);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.frame_Fname = QFrame(self.frame_features_one_employee)
        self.frame_Fname.setObjectName(u"frame_Fname")
        self.frame_Fname.setGeometry(QRect(80, 110, 291, 61))
        self.frame_Fname.setFrameShape(QFrame.StyledPanel)
        self.frame_Fname.setFrameShadow(QFrame.Raised)
        self.lineEdit_fname = QLineEdit(self.frame_Fname)
        self.lineEdit_fname.setObjectName(u"lineEdit_fname")
        self.lineEdit_fname.setGeometry(QRect(90, 10, 185, 48))
        self.lineEdit_fname.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color:rgb(39, 53, 62);\n"
"font-size: 18px;\n"
"color:rgb(255, 255, 255);\n"
"qproperty-alignment: AlignCenter}")
        self.label = QLabel(self.frame_Fname)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 75, 34))
        self.label.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.frame_Lname = QFrame(self.frame_features_one_employee)
        self.frame_Lname.setObjectName(u"frame_Lname")
        self.frame_Lname.setGeometry(QRect(80, 180, 291, 61))
        self.frame_Lname.setFrameShape(QFrame.StyledPanel)
        self.frame_Lname.setFrameShadow(QFrame.Raised)
        self.lineEdit_Lname = QLineEdit(self.frame_Lname)
        self.lineEdit_Lname.setObjectName(u"lineEdit_Lname")
        self.lineEdit_Lname.setGeometry(QRect(90, 10, 185, 48))
        self.lineEdit_Lname.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color:rgb(39, 53, 62);\n"
"font-size: 18px;\n"
"color:rgb(255, 255, 255);\n"
"qproperty-alignment: AlignCenter}\n"
"                                      ")
        self.label_3 = QLabel(self.frame_Lname)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 0, 75, 34))
        self.label_3.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.frame_RFID = QFrame(self.frame_features_one_employee)
        self.frame_RFID.setObjectName(u"frame_RFID")
        self.frame_RFID.setGeometry(QRect(70, 250, 291, 61))
        self.frame_RFID.setFrameShape(QFrame.StyledPanel)
        self.frame_RFID.setFrameShadow(QFrame.Raised)
        self.label_RFID = QLabel(self.frame_RFID)
        self.label_RFID.setObjectName(u"label_RFID")
        self.label_RFID.setGeometry(QRect(100, 10, 185, 48))
        self.label_RFID.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"color:rgb(255, 255, 255);\n"
"qproperty-alignment: AlignCenter;")
        self.label_5 = QLabel(self.frame_RFID)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 0, 75, 34))
        self.label_5.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.frame_fingerprint = QFrame(self.frame_features_one_employee)
        self.frame_fingerprint.setObjectName(u"frame_fingerprint")
        self.frame_fingerprint.setGeometry(QRect(100, 450, 251, 61))
        self.frame_fingerprint.setFrameShape(QFrame.StyledPanel)
        self.frame_fingerprint.setFrameShadow(QFrame.Raised)
        self.label_id_fingerprint = QLabel(self.frame_fingerprint)
        self.label_id_fingerprint.setObjectName(u"label_id_fingerprint")
        self.label_id_fingerprint.setGeometry(QRect(100, 10, 141, 47))
        self.label_id_fingerprint.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 18px;\n"
"color: rgb(255, 255, 255);\n"
"qproperty-alignment: AlignCenter")
        self.label_12 = QLabel(self.frame_fingerprint)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 0, 75, 34))
        self.label_12.setStyleSheet(u"\n"
"background-color:rgb(0, 173, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")
        self.label_7 = QLabel(self.frame_features_one_employee)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 400, 71, 31))
        self.label_7.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(0, 173, 239);")
        self.label_message_number_fingerprint = QLabel(self.frame_features_one_employee)
        self.label_message_number_fingerprint.setObjectName(u"label_message_number_fingerprint")
        self.label_message_number_fingerprint.setGeometry(QRect(200, 520, 151, 20))
        self.label_message_number_fingerprint.setStyleSheet(u"color: rgb(206, 206, 206);\n"
"")
        self.pushButton_save = QPushButton(self.frame_features_one_employee)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(0, 720, 561, 81))
        self.pushButton_save.setStyleSheet(u"QPushButton#pushButton_save{\n"
"background: rgba(0, 173, 239, 0.3);\n"
"border-radius: 6.80774px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton#pushButton_save:pressed {\n"
"    background-color: rgb(127, 132, 137);\n"
"    border-style: inset;\n"
"}")
        self.pushButton_save_finger = QPushButton(self.frame_features_one_employee)
        self.pushButton_save_finger.setObjectName(u"pushButton_save_finger")
        self.pushButton_save_finger.setGeometry(QRect(330, 440, 99, 96))
        self.pushButton_save_finger.setStyleSheet(u"border-radius: 13px;")
        icon1 = QIcon()
        icon1.addFile(u":/fingerprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save_finger.setIcon(icon1)
        self.pushButton_save_finger.setIconSize(QSize(99, 96))
        self.checkBox_active = QCheckBox(self.frame_features_one_employee)
        self.checkBox_active.setObjectName(u"checkBox_active")
        self.checkBox_active.setGeometry(QRect(440, 20, 51, 31))
        self.checkBox_active.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/switch_able.png)\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/switch_disable.png)\n"
"}")
        ########first page###############3

        self.fram_first_time = QFrame(self.centralwidget)
        self.fram_first_time.setObjectName(u"fram_first_time")
        self.fram_first_time.setGeometry(QRect(770, 30, 401, 651))
        self.fram_first_time.setFrameShape(QFrame.StyledPanel)
        self.fram_first_time.setFrameShadow(QFrame.Raised)
        self.label_text_first = QLabel(self.fram_first_time)
        self.label_text_first.setObjectName(u"label_text_first")
        self.label_text_first.setGeometry(QRect(70, 250, 331, 111))
        self.label_text_first.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"MS Shell Dlg 2\";")
        self.label_2_text_first = QLabel(self.fram_first_time)
        self.label_2_text_first.setObjectName(u"label_2_text_first")
        self.label_2_text_first.setGeometry(QRect(110, 450, 51, 20))
        self.label_2_text_first.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                              "font: 10pt \"MS Shell Dlg 2\";")
        self.button_add_first = QPushButton(self.fram_first_time)
        self.button_add_first.setObjectName(u"button_add_first")
        self.button_add_first.setGeometry(QRect(200, 440, 41, 41))
        self.button_add_first.setStyleSheet(u"border-radius: 30px;")
        self.button_add_first.setIcon(icon)
        self.button_add_first.setIconSize(QSize(40, 40))

        self.label_erro_fill = QLabel(self.frame_features_one_employee)
        self.label_erro_fill.setObjectName(u"label_erro_fill")
        self.label_erro_fill.setGeometry(QRect(140, 340, 251, 21))
        self.label_erro_fill.setStyleSheet(u"\n"
                                           "color: rgb(255, 255, 127);")


        self.label_4 = QLabel(self.frame_features_one_employee)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 20, 51, 31))
        self.label_4.setStyleSheet(u"color: rgb(0, 173, 239);")
        self.pushButton_export = QPushButton(self.frame_features_one_employee)
        self.pushButton_export.setObjectName(u"pushButton_export")
        self.pushButton_export.setGeometry(QRect(490, 20, 51, 41))
        self.pushButton_export.setStyleSheet(u"border-radius: 13px;")
        icon2 = QIcon()
        icon2.addFile(u":/exportButton.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_export.setIcon(icon2)
        self.pushButton_export.setIconSize(QSize(42, 42))
        self.image_admin = QLabel(self.centralwidget)
        self.image_admin.setObjectName(u"image_admin")
        self.image_admin.setGeometry(QRect(53, 28, 81, 81))
        self.image_admin.setStyleSheet(u"background-image: url(:/rsz_arash_golsaz.png);\n"
"border-radius: 40px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon_dashboard.setText("")
        self.icon_setting.setText("")
        self.icon_dashboard_3.setText("")
        self.pushButton_admin_employee.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.pushButton_Adashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_Asetting.setText(QCoreApplication.translate("MainWindow", u"Settimg", None))
        self.pushButton_5.setText("")
        self.employee1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.employee3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_t_name.setText(QCoreApplication.translate("MainWindow", u"Fill", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" ", None))
        self.lineEdit_fname.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Fname</p></body></html>", None))
        self.lineEdit_Lname.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Lname</p></body></html>", None))
        self.label_RFID.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">RFID</p></body></html>", None))
        self.label_id_fingerprint.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ID</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fingeprint", None))
        self.label_message_number_fingerprint.setText(QCoreApplication.translate("MainWindow", u"No fingerprint saved", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_save_finger.setText("")
        self.checkBox_active.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"active", None))
        self.pushButton_export.setText("")
        self.image_admin.setText("")
        self.label_text_first.setText(QCoreApplication.translate("MainWindow", u"please add your first employee", None))
        self.label_2_text_first.setText(QCoreApplication.translate("MainWindow", u"press", None))
        self.button_add_first.setText("")
        self.label_erro_fill.setText("")
        self.employee1.hide()
        self.employee2.hide()
        self.employee3.hide()
        self.employee4.hide()
        self.employee5.hide()
        self.employee6.hide()
        self.employee7.hide()
        self.employee8.hide()

    def add_framEmployee_array(self):

        array_framEmployee=[]
        array_framEmployee.append(self.employee1)
        array_framEmployee.append(self.employee2)
        array_framEmployee.append(self.employee3)
        array_framEmployee.append(self.employee4)
        array_framEmployee.append(self.employee5)
        array_framEmployee.append(self.employee6)
        array_framEmployee.append(self.employee7)
        array_framEmployee.append(self.employee8)

        return array_framEmployee

    # retranslateUi


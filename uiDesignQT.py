# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'artaprojectwLahbI.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/backgroubd.png"))
        self.button_door = QPushButton(self.centralwidget)
        self.button_door.setObjectName(u"button_door")
        self.button_door.setGeometry(QRect(640, 730, 211, 201))
        self.button_door.setStyleSheet(u"\n"
"border-radius: 100px;\n"
"")
        icon = QIcon()
        icon.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/Lockbtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_door.setIcon(icon)
        self.button_door.setIconSize(QSize(243, 252))
        self.button_lamp1 = QPushButton(self.centralwidget)
        self.button_lamp1.setObjectName(u"button_lamp1")
        self.button_lamp1.setGeometry(QRect(538, 196, 90, 90))
        self.button_lamp1.setStyleSheet(u"\n"
"border-radius: 30px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btLampOff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_lamp1.setIcon(icon1)
        self.button_lamp1.setIconSize(QSize(90, 90))
        self.button_AC = QPushButton(self.centralwidget)
        self.button_AC.setObjectName(u"button_AC")
        self.button_AC.setGeometry(QRect(888, 196, 101, 101))
        self.button_AC.setStyleSheet(u"\n"
"border-radius: 30px;")
        icon2 = QIcon()
        icon2.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btAC2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_AC.setIcon(icon2)
        self.button_AC.setIconSize(QSize(90, 90))
        self.button_lamp3 = QPushButton(self.centralwidget)
        self.button_lamp3.setObjectName(u"button_lamp3")
        self.button_lamp3.setGeometry(QRect(771, 196, 101, 101))
        self.button_lamp3.setStyleSheet(u"\n"
"border-radius: 30px;")
        icon3 = QIcon()
        icon3.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btLampOff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_lamp3.setIcon(icon3)
        self.button_lamp3.setIconSize(QSize(90, 90))
        self.button_lamp4 = QPushButton(self.centralwidget)
        self.button_lamp4.setObjectName(u"button_lamp4")
        self.button_lamp4.setGeometry(QRect(888, 196, 101, 101))
        self.button_lamp4.setStyleSheet(u"\n"
"border-radius: 30px;")
        self.button_lamp4.setIcon(icon3)
        self.button_lamp4.setIconSize(QSize(90, 90))
        self.button_lamp7 = QPushButton(self.centralwidget)
        self.button_lamp7.setObjectName(u"button_lamp7")
        self.button_lamp7.setGeometry(QRect(771, 324, 101, 101))
        self.button_lamp7.setStyleSheet(u"\n"
"\n"
"border-radius: 30px;")
        self.button_lamp7.setIcon(icon3)
        self.button_lamp7.setIconSize(QSize(90, 90))
        self.button_lamp6 = QPushButton(self.centralwidget)
        self.button_lamp6.setObjectName(u"button_lamp6")
        self.button_lamp6.setGeometry(QRect(655, 324, 101, 101))
        self.button_lamp6.setStyleSheet(u"\n"
"border-radius: 30px;")
        self.button_lamp6.setIcon(icon3)
        self.button_lamp6.setIconSize(QSize(90, 90))
        self.button_lamp5 = QPushButton(self.centralwidget)
        self.button_lamp5.setObjectName(u"button_lamp5")
        self.button_lamp5.setGeometry(QRect(538, 324, 101, 101))
        self.button_lamp5.setStyleSheet(u"\n"
"border-radius: 30px;")
        self.button_lamp5.setIcon(icon3)
        self.button_lamp5.setIconSize(QSize(90, 90))
        self.button_lamp2 = QPushButton(self.centralwidget)
        self.button_lamp2.setObjectName(u"button_lamp2")
        self.button_lamp2.setGeometry(QRect(655, 196, 101, 101))
        self.button_lamp2.setStyleSheet(u"\n"
"\n"
"border-radius: 30px;")
        self.button_lamp2.setIcon(icon3)
        self.button_lamp2.setIconSize(QSize(90, 90))
        self.button_power = QPushButton(self.centralwidget)
        self.button_power.setObjectName(u"button_power")
        self.button_power.setGeometry(QRect(840, 550, 101, 101))
        self.button_power.setStyleSheet(u"\n"
"border-radius: 30px;")
        icon4 = QIcon()
        icon4.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btPoweroff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_power.setIcon(icon4)
        self.button_power.setIconSize(QSize(90, 90))
        self.label_power = QLabel(self.centralwidget)
        self.label_power.setObjectName(u"label_power")
        self.label_power.setGeometry(QRect(573, 563, 91, 21))
        self.label_power.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Segoe MDL2 Assets\";\n"
"")
        self.label_FixText = QLabel(self.centralwidget)
        self.label_FixText.setObjectName(u"label_FixText")
        self.label_FixText.setGeometry(QRect(573, 604, 101, 31))
        self.label_FixText.setStyleSheet(u"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.label_lamp1 = QLabel(self.centralwidget)
        self.label_lamp1.setObjectName(u"label_lamp1")
        self.label_lamp1.setGeometry(QRect(558, 158, 41, 31))
        self.label_lamp1.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_lamp3 = QLabel(self.centralwidget)
        self.label_lamp3.setObjectName(u"label_lamp3")
        self.label_lamp3.setGeometry(QRect(800, 160, 41, 31))
        self.label_lamp3.setStyleSheet(u"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.label_lamp2 = QLabel(self.centralwidget)
        self.label_lamp2.setObjectName(u"label_lamp2")
        self.label_lamp2.setGeometry(QRect(680, 170, 41, 16))
        self.label_lamp2.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_lamp4 = QLabel(self.centralwidget)
        self.label_lamp4.setObjectName(u"label_lamp4")
        self.label_lamp4.setGeometry(QRect(920, 170, 41, 16))
        self.label_lamp4.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_lamp5 = QLabel(self.centralwidget)
        self.label_lamp5.setObjectName(u"label_lamp5")
        self.label_lamp5.setGeometry(QRect(560, 300, 55, 16))
        self.label_lamp5.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_lamp6 = QLabel(self.centralwidget)
        self.label_lamp6.setObjectName(u"label_lamp6")
        self.label_lamp6.setGeometry(QRect(680, 300, 55, 16))
        self.label_lamp6.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_lamp7 = QLabel(self.centralwidget)
        self.label_lamp7.setObjectName(u"label_lamp7")
        self.label_lamp7.setGeometry(QRect(800, 300, 55, 16))
        self.label_lamp7.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_AC = QLabel(self.centralwidget)
        self.label_AC.setObjectName(u"label_AC")
        self.label_AC.setGeometry(QRect(930, 300, 21, 16))
        self.label_AC.setStyleSheet(u"QLabel {\n"
"color:#7F8489;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_AC.setTextFormat(Qt.AutoText)
        self.button_AC.setIconSize(QSize(90, 90))
        self.label_sayGood = QLabel(self.centralwidget)
        self.label_sayGood.setObjectName(u"label_sayGood")
        self.label_sayGood.setGeometry(QRect(1350, 810, 421, 101))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(36)
        self.label_sayGood.setFont(font1)
        self.label_sayGood.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.circularProgressH = QFrame(self.centralwidget)
        self.circularProgressH.setObjectName(u"circularProgressH")
        self.circularProgressH.setGeometry(QRect(1280, 500, 230, 230))
        self.circularProgressH.setStyleSheet(u"border-radius:115px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 85, 255, 0), stop:0.75 rgba(115, 161, 206, 255));")
        self.circularProgressH.setFrameShape(QFrame.NoFrame)
        self.circularProgressH.setFrameShadow(QFrame.Raised)
        self.containerH = QFrame(self.circularProgressH)
        self.containerH.setObjectName(u"containerH")
        self.containerH.setGeometry(QRect(15, 15, 200, 200))
        self.containerH.setStyleSheet(u"QFrame{\n"
"background-color: rgb(29, 45, 53);\n"
"border-radius:100px;\n"
"}")
        self.containerH.setFrameShape(QFrame.StyledPanel)
        self.containerH.setFrameShadow(QFrame.Raised)
        self.label_fix_logo_humidity = QLabel(self.containerH)
        self.label_fix_logo_humidity.setObjectName(u"label_fix_logo_humidity")
        self.label_fix_logo_humidity.setGeometry(QRect(30, 60, 81, 61))
        self.label_fix_logo_humidity.setBaseSize(QSize(10, 10))
        self.label_fix_logo_humidity.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/humidity.svg"))
        self.label_humidity = QLabel(self.containerH)
        self.label_humidity.setObjectName(u"label_humidity")
        self.label_humidity.setGeometry(QRect(70, 40, 71, 81))
        self.label_humidity.setStyleSheet(u"color: rgb(234, 234, 235);\n"
"\n"
"font: 25 40pt \"Segoe UI Light\";")
        self.label_fix_persent = QLabel(self.containerH)
        self.label_fix_persent.setObjectName(u"label_fix_persent")
        self.label_fix_persent.setGeometry(QRect(140, 60, 31, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(10)
        self.label_fix_persent.setFont(font2)
        self.label_fix_humidity = QLabel(self.containerH)
        self.label_fix_humidity.setObjectName(u"label_fix_humidity")
        self.label_fix_humidity.setGeometry(QRect(50, 130, 91, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Light")
        font3.setPointSize(16)
        self.label_fix_humidity.setFont(font3)
        self.label_fix_logo_humidity.raise_()
        self.label_humidity.raise_()
        self.label_fix_humidity.raise_()
        self.label_fix_persent.raise_()
        self.circularBgH = QFrame(self.centralwidget)
        self.circularBgH.setObjectName(u"circularBgH")
        self.circularBgH.setGeometry(QRect(1280, 500, 230, 230))
        self.circularBgH.setStyleSheet(u"background-color: rgba(84, 88, 92,120);\n"
"border-radius:115px;\n"
"")
        self.circularBgH.setFrameShape(QFrame.NoFrame)
        self.circularBgH.setFrameShadow(QFrame.Raised)
        self.frame_T = QFrame(self.centralwidget)
        self.frame_T.setObjectName(u"frame_T")
        self.frame_T.setGeometry(QRect(1600, 500, 230, 230))
        self.frame_T.setStyleSheet(u"background-color: rgba(84, 88, 92,120);\n"
"border-radius:115px;\n"
"")
        self.frame_T.setFrameShape(QFrame.NoFrame)
        self.frame_T.setFrameShadow(QFrame.Raised)
        self.circularProgressT = QFrame(self.frame_T)
        self.circularProgressT.setObjectName(u"circularProgressT")
        self.circularProgressT.setGeometry(QRect(0, 0, 230, 230))
        self.circularProgressT.setStyleSheet(u"border-radius:115px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 85, 255, 0), stop:0.75 rgba(253, 54, 11, 80));\n"
"\n"
"")
        self.circularProgressT.setFrameShape(QFrame.NoFrame)
        self.circularProgressT.setFrameShadow(QFrame.Raised)
        self.containerT = QFrame(self.circularProgressT)
        self.containerT.setObjectName(u"containerT")
        self.containerT.setGeometry(QRect(15, 15, 200, 200))
        self.containerT.setStyleSheet(u"QFrame{\n"
"background-color: rgb(29, 45, 53);\n"
"border-radius:100px;\n"
"}")
        self.containerT.setFrameShape(QFrame.StyledPanel)
        self.containerT.setFrameShadow(QFrame.Raised)
        self.label_fix_logo_temperature = QLabel(self.containerT)
        self.label_fix_logo_temperature.setObjectName(u"label_fix_logo_temperature")
        self.label_fix_logo_temperature.setGeometry(QRect(20, 60, 51, 61))
        self.label_fix_logo_temperature.setBaseSize(QSize(10, 10))
        self.label_fix_logo_temperature.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/temperaturelogo.svg"))
        self.label_temperature = QLabel(self.containerT)
        self.label_temperature.setObjectName(u"label_temperature")
        self.label_temperature.setGeometry(QRect(70, 40, 111, 81))
        self.label_temperature.setStyleSheet(u"color: rgb(234, 234, 235);\n"
"\n"
"font: 25 40pt \"Segoe UI Light\";")
        self.label_fix_logo_degree = QLabel(self.containerT)
        self.label_fix_logo_degree.setObjectName(u"label_fix_logo_degree")
        self.label_fix_logo_degree.setGeometry(QRect(140, 60, 31, 21))
        self.label_fix_logo_degree.setFont(font2)
        self.label_fix_temperature = QLabel(self.containerT)
        self.label_fix_temperature.setObjectName(u"label_fix_temperature")
        self.label_fix_temperature.setGeometry(QRect(30, 120, 141, 41))
        self.label_fix_temperature.setFont(font3)
        self.label_hour = QLabel(self.centralwidget)
        self.label_hour.setObjectName(u"label_hour")
        self.label_hour.setGeometry(QRect(10, 10, 61, 81))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Light")
        font4.setPointSize(38)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(3)
        self.label_hour.setFont(font4)
        self.label_hour.setStyleSheet(u"font: 25 38pt \"Segoe UI Light\";\n"
" color:#eaeaeb;")
        self.label_minute = QLabel(self.centralwidget)
        self.label_minute.setObjectName(u"label_minute")
        self.label_minute.setGeometry(QRect(10, 80, 81, 71))
        self.label_minute.setStyleSheet(u"\n"
"font: 87 36pt \"Segoe UI Black\";\n"
" color:#eaeaeb;")
        self.label_year = QLabel(self.centralwidget)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setGeometry(QRect(10, 180, 61, 31))
        self.label_year.setStyleSheet(u"font: 25 18pt \"Segoe UI Light\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 180, 31, 31))
        self.label_3.setStyleSheet(u"font: 25 18pt \"Segoe UI Light\";\n"
"color:rgb(65, 187, 255)")
        self.label_day = QLabel(self.centralwidget)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setGeometry(QRect(120, 180, 41, 31))
        self.label_day.setStyleSheet(u"font: 25 18pt \"Segoe UI Light\";\n"
"color: rgb(255, 255, 255);")
        self.label_fix_opendoor = QLabel(self.centralwidget)
        self.label_fix_opendoor.setObjectName(u"label_fix_opendoor")
        self.label_fix_opendoor.setGeometry(QRect(650, 920, 201, 21))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Light")
        self.label_fix_opendoor.setFont(font5)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1750, 30, 160, 87))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_wifi = QLabel(self.frame)
        self.label_wifi.setObjectName(u"label_wifi")
        self.label_wifi.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/wifi.svg"))

        self.horizontalLayout.addWidget(self.label_wifi)

        self.pushButton_setting = QPushButton(self.frame)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setStyleSheet(u"\n"
"border-radius: 100px;")
        icon5 = QIcon()
        icon5.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/Settings (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setting.setIcon(icon5)
        self.pushButton_setting.setIconSize(QSize(70, 70))

        self.horizontalLayout.addWidget(self.pushButton_setting)

        self.pushButton_setting.raise_()
        self.label_wifi.raise_()
        self.frame_employees = QFrame(self.centralwidget)
        self.frame_employees.setObjectName(u"frame_employees")
        self.frame_employees.setGeometry(QRect(10, 590, 341, 391))
        self.frame_employees.setFrameShape(QFrame.NoFrame)
        self.frame_employees.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_employees)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.frame_eployee_2 = QFrame(self.frame_employees)
#         self.frame_eployee_2.setObjectName(u"frame_eployee_2")
#         self.frame_eployee_2.setStyleSheet(u"color:rgb(85, 170, 255)")
#         self.frame_eployee_2.setFrameShape(QFrame.StyledPanel)
#         self.frame_eployee_2.setFrameShadow(QFrame.Raised)
#         self.label_fix_logo_user_3 = QLabel(self.frame_eployee_2)
#         self.label_fix_logo_user_3.setObjectName(u"label_fix_logo_user_3")
#         self.label_fix_logo_user_3.setGeometry(QRect(10, 0, 41, 41))
#         self.label_fix_logo_user_3.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/user.svg"))
#         self.label_name_employee_3 = QLabel(self.frame_eployee_2)
#         self.label_name_employee_3.setObjectName(u"label_name_employee_3")
#         self.label_name_employee_3.setGeometry(QRect(60, 10, 101, 21))
#         self.label_name_employee_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
# "font: 25 10pt \"Segoe UI Light\";")
#         self.label_tim_login_3 = QLabel(self.frame_eployee_2)
#         self.label_tim_login_3.setObjectName(u"label_tim_login_3")
#         self.label_tim_login_3.setGeometry(QRect(200, 10, 41, 21))
#         self.label_tim_login_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
# "font: 25 10pt \"Segoe UI Light\";")
#         self.label_time_logOut_3 = QLabel(self.frame_eployee_2)
#         self.label_time_logOut_3.setObjectName(u"label_time_logOut_3")
#         self.label_time_logOut_3.setGeometry(QRect(250, 10, 61, 21))
#         self.label_time_logOut_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
# "font: 25 10pt \"Segoe UI Light\";")
#
#         self.verticalLayout.addWidget(self.frame_eployee_2)
#
#         self.frame_eployee = QFrame(self.frame_employees)
#         self.frame_eployee.setObjectName(u"frame_eployee")
#         self.frame_eployee.setStyleSheet(u"color:rgb(85, 170, 255)")
#         self.frame_eployee.setFrameShape(QFrame.StyledPanel)
#         self.frame_eployee.setFrameShadow(QFrame.Raised)
#         self.label_fix_logo_user = QLabel(self.frame_eployee)
#         self.label_fix_logo_user.setObjectName(u"label_fix_logo_user")
#         self.label_fix_logo_user.setGeometry(QRect(10, 0, 41, 41))
#         self.label_fix_logo_user.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/user.svg"))
#         self.label_name_employee = QLabel(self.frame_eployee)
#         self.label_name_employee.setObjectName(u"label_name_employee")
#         self.label_name_employee.setGeometry(QRect(60, 10, 101, 21))
#         self.label_name_employee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
# "font: 25 10pt \"Segoe UI Light\";")
#         self.label_tim_login = QLabel(self.frame_eployee)
#         self.label_tim_login.setObjectName(u"label_tim_login")
#         self.label_tim_login.setGeometry(QRect(200, 10, 41, 21))
#         self.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
# "font: 25 10pt \"Segoe UI Light\";")
#         self.label_time_logOut = QLabel(self.frame_eployee)
#         self.label_time_logOut.setObjectName(u"label_time_logOut")
#         self.label_time_logOut.setGeometry(QRect(260, 10, 51, 21))
#         self.label_time_logOut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
# "font: 25 10pt \"Segoe UI Light\";")
#
#         self.verticalLayout.addWidget(self.frame_eployee)

        # self.verticalLayout.setStretch(0, 1)
        # self.verticalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.button_door.raise_()
        self.button_lamp1.raise_()
        self.button_AC.raise_()
        self.button_lamp3.raise_()
        self.button_lamp4.raise_()
        self.button_lamp7.raise_()
        self.button_lamp6.raise_()
        self.button_lamp5.raise_()
        self.button_lamp2.raise_()
        self.button_power.raise_()
        self.label_power.raise_()
        self.label_FixText.raise_()
        self.label_lamp1.raise_()
        self.label_lamp3.raise_()
        self.label_lamp2.raise_()
        self.label_lamp4.raise_()
        self.label_lamp5.raise_()
        self.label_lamp6.raise_()
        self.label_lamp7.raise_()
        self.label_AC.raise_()
        self.label_sayGood.raise_()
        self.circularBgH.raise_()
        self.circularProgressH.raise_()
        self.frame_T.raise_()
        self.label_hour.raise_()
        self.label_minute.raise_()
        self.label_year.raise_()
        self.label_3.raise_()
        self.label_day.raise_()
        self.label_fix_opendoor.raise_()
        self.frame.raise_()
        self.frame_employees.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.button_door.setText("")
        self.button_lamp1.setText("")
        self.button_AC.setText("")
        self.button_lamp3.setText("")
        self.button_lamp4.setText("")
        self.button_lamp7.setText("")
        self.button_lamp6.setText("")
        self.button_lamp5.setText("")
        self.button_lamp2.setText("")
        self.button_power.setText("")
        self.label_power.setText(QCoreApplication.translate("MainWindow", u"Turn off", None))
        self.label_FixText.setText(QCoreApplication.translate("MainWindow", u"All of points", None))
        self.label_lamp1.setText(QCoreApplication.translate("MainWindow", u"lapm1", None))
        self.label_lamp3.setText(QCoreApplication.translate("MainWindow", u"lamp3", None))
        self.label_lamp2.setText(QCoreApplication.translate("MainWindow", u"lapm2", None))
        self.label_lamp4.setText(QCoreApplication.translate("MainWindow", u"lamp4", None))
        self.label_lamp5.setText(QCoreApplication.translate("MainWindow", u"lamp5", None))
        self.label_lamp6.setText(QCoreApplication.translate("MainWindow", u"lamp6", None))
        self.label_lamp7.setText(QCoreApplication.translate("MainWindow", u"lamp7", None))
        self.label_AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.label_sayGood.setText(QCoreApplication.translate("MainWindow", u" Good morning", None))
        self.label_fix_logo_humidity.setText("")
        self.label_humidity.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_fix_persent.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#969696;\">%</span></p></body></html>", None))
        self.label_fix_humidity.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#eaeaeb;\">Humidity</span></p></body></html>", None))
        self.label_fix_logo_temperature.setText("")
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_fix_logo_degree.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI Light'; font-size:10pt; color:#969696;\">\u00b0C</span></p></body></html>", None))
        self.label_fix_temperature.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ddddde;\">Temperature</span></p></body></html>", None))
        self.label_hour.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_minute.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"1400", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"07", None))
        self.label_day.setText(QCoreApplication.translate("MainWindow", u"04", None))
        self.label_fix_opendoor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#e6e6e6;\">Tap to open the door</span></p></body></html>", None))
        self.label_wifi.setText("")
        self.pushButton_setting.setText("")
        # self.label_fix_logo_user_3.setText("")
        # self.label_name_employee_3.setText(QCoreApplication.translate("MainWindow", u"Arash Golsaz", None))
        # self.label_tim_login_3.setText(QCoreApplication.translate("MainWindow", u"08:34", None))
        # self.label_time_logOut_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">08:34</p></body></html>", None))
        # self.label_fix_logo_user.setText("")
        # self.label_name_employee.setText(QCoreApplication.translate("MainWindow", u"Arash Golsaz", None))
        # self.label_tim_login.setText(QCoreApplication.translate("MainWindow", u"08:34", None))
        # self.label_time_logOut.setText(QCoreApplication.translate("MainWindow", u"08:34", None))
    # retranslateUi

    def change_icon_lamp(self):
            # global icon_light_on, icon_light_off
            self.icon_light_on = QIcon()
            self.icon_light_off = QIcon()
            self.icon_light_on.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btnLamp2.png", QSize(), QIcon.Normal,
                                  QIcon.Off)
            self.icon_light_off.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btLampOff.png", QSize(), QIcon.Normal,
                                   QIcon.Off)



    #----------------------bular


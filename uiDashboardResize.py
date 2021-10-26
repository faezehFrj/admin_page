# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'artaproject_resizeNbOTWt.ui'
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

import resources_dashboard


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 802)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
                                         "background-image: url(:/Dashboard.png);}")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.button_lamp1 = QPushButton(self.frame)
        self.button_lamp1.setObjectName(u"button_lamp1")
        self.button_lamp1.setGeometry(QRect(350, 140, 71, 61))
        self.button_lamp1.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        icon = QIcon()
        icon.addFile(u":/btn_off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_lamp1.setIcon(icon)
        self.button_lamp1.setIconSize(QSize(60, 60))
        self.button_lamp2 = QPushButton(self.frame)
        self.button_lamp2.setObjectName(u"button_lamp2")
        self.button_lamp2.setGeometry(QRect(430, 140, 71, 61))
        self.button_lamp2.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp2.setIcon(icon)
        self.button_lamp2.setIconSize(QSize(60, 60))
        self.button_lamp3 = QPushButton(self.frame)
        self.button_lamp3.setObjectName(u"button_lamp3")
        self.button_lamp3.setGeometry(QRect(510, 140, 71, 61))
        self.button_lamp3.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp3.setIcon(icon)
        self.button_lamp3.setIconSize(QSize(60, 60))
        self.button_lamp4 = QPushButton(self.frame)
        self.button_lamp4.setObjectName(u"button_lamp4")
        self.button_lamp4.setGeometry(QRect(590, 140, 71, 61))
        self.button_lamp4.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp4.setIcon(icon)
        self.button_lamp4.setIconSize(QSize(60, 60))
        self.label_lamp1 = QLabel(self.frame)
        self.label_lamp1.setObjectName(u"label_lamp1")
        self.label_lamp1.setGeometry(QRect(370, 110, 41, 16))
        self.label_lamp1.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.label_lamp2 = QLabel(self.frame)
        self.label_lamp2.setObjectName(u"label_lamp2")
        self.label_lamp2.setGeometry(QRect(450, 110, 41, 16))
        self.label_lamp2.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.label_lamp3 = QLabel(self.frame)
        self.label_lamp3.setObjectName(u"label_lamp3")
        self.label_lamp3.setGeometry(QRect(530, 110, 41, 16))
        self.label_lamp3.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.label_lamp4 = QLabel(self.frame)
        self.label_lamp4.setObjectName(u"label_lamp4")
        self.label_lamp4.setGeometry(QRect(610, 110, 41, 16))
        self.label_lamp4.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.button_lamp5 = QPushButton(self.frame)
        self.button_lamp5.setObjectName(u"button_lamp5")
        self.button_lamp5.setGeometry(QRect(350, 250, 71, 61))
        self.button_lamp5.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp5.setIcon(icon)
        self.button_lamp5.setIconSize(QSize(60, 60))
        self.button_lamp6 = QPushButton(self.frame)
        self.button_lamp6.setObjectName(u"button_lamp6")
        self.button_lamp6.setGeometry(QRect(430, 250, 71, 61))
        self.button_lamp6.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp6.setIcon(icon)
        self.button_lamp6.setIconSize(QSize(60, 60))
        self.button_lamp7 = QPushButton(self.frame)
        self.button_lamp7.setObjectName(u"button_lamp7")
        self.button_lamp7.setGeometry(QRect(510, 250, 71, 61))
        self.button_lamp7.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp7.setIcon(icon)
        self.button_lamp7.setIconSize(QSize(60, 60))
        self.button_lamp8 = QPushButton(self.frame)
        self.button_lamp8.setObjectName(u"button_lamp8")
        self.button_lamp8.setGeometry(QRect(590, 250, 71, 61))
        self.button_lamp8.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        self.button_lamp8.setIcon(icon)
        self.button_lamp8.setIconSize(QSize(60, 60))
        self.label_lamp5 = QLabel(self.frame)
        self.label_lamp5.setObjectName(u"label_lamp5")
        self.label_lamp5.setGeometry(QRect(370, 220, 41, 16))
        self.label_lamp5.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.label_lamp6 = QLabel(self.frame)
        self.label_lamp6.setObjectName(u"label_lamp6")
        self.label_lamp6.setGeometry(QRect(450, 220, 41, 16))
        self.label_lamp6.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.label_lamp7 = QLabel(self.frame)
        self.label_lamp7.setObjectName(u"label_lamp7")
        self.label_lamp7.setGeometry(QRect(530, 220, 41, 16))
        self.label_lamp7.setStyleSheet(u"QLabel {\n"
                                       "color:#7F8489;\n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "}")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(610, 220, 41, 16))
        self.label_12.setStyleSheet(u"QLabel {\n"
                                    "color:#7F8489;\n"
                                    "font: 8pt \"MS Shell Dlg 2\";\n"
                                    "}")
        self.button_power = QPushButton(self.frame)
        self.button_power.setObjectName(u"button_power")
        self.button_power.setGeometry(QRect(560, 380, 71, 61))
        self.button_power.setStyleSheet(u"\n"
                                        "border-radius: 30px;\n"
                                        "")
        icon1 = QIcon()
        icon1.addFile(u":/Dry_power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_power.setIcon(icon1)
        self.button_power.setIconSize(QSize(60, 60))
        self.label_FixText = QLabel(self.frame)
        self.label_FixText.setObjectName(u"label_FixText")
        self.label_FixText.setGeometry(QRect(380, 410, 81, 31))
        self.label_FixText.setStyleSheet(u"color:#7F8489;\n"
                                         "font: 7pt \"MS Shell Dlg 2\";")
        self.label_power = QLabel(self.frame)
        self.label_power.setObjectName(u"label_power")
        self.label_power.setGeometry(QRect(380, 380, 91, 21))
        self.label_power.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                       "font: 75 11pt \"Segoe MDL2 Assets\";\n"
                                       "")
        self.button_door = QPushButton(self.frame)
        self.button_door.setObjectName(u"button_door")
        self.button_door.setGeometry(QRect(430, 500, 141, 141))
        self.button_door.setStyleSheet(u"\n"
                                       "border-radius: 100px;\n"
                                       "")
        icon2 = QIcon()
        icon2.addFile(u":/Lock btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_door.setIcon(icon2)
        self.button_door.setIconSize(QSize(170, 171))
        self.label_fix_opendoor = QLabel(self.frame)
        self.label_fix_opendoor.setObjectName(u"label_fix_opendoor")
        self.label_fix_opendoor.setGeometry(QRect(420, 650, 171, 21))
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        self.label_fix_opendoor.setFont(font)
        self.label_hour = QLabel(self.frame)
        self.label_hour.setObjectName(u"label_hour")
        self.label_hour.setGeometry(QRect(20, 0, 81, 81))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(34)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(2)
        self.label_hour.setFont(font1)
        self.label_hour.setStyleSheet(u"font: 20 34pt \"Segoe UI Light\";\n"
                                      "color:#eaeaeb;\n"
                                      "")
        self.label_minute = QLabel(self.frame)
        self.label_minute.setObjectName(u"label_minute")
        self.label_minute.setGeometry(QRect(20, 50, 81, 91))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(34)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(2)
        self.label_minute.setFont(font2)
        self.label_minute.setStyleSheet(u"font: 20 34pt \"Segoe UI Black\";\n"
                                        "color:#eaeaeb;")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 170, 31, 31))
        self.label_13.setStyleSheet(u"font: 25 16pt \"Segoe UI Light\";\n"
                                    "color:rgb(65, 187, 255)")
        self.label_year = QLabel(self.frame)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setGeometry(QRect(20, 170, 61, 31))
        self.label_year.setStyleSheet(u"font: 25 16pt \"Segoe UI Light\";\n"
                                      "color: rgb(255, 255, 255);")
        self.label_day = QLabel(self.frame)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setGeometry(QRect(120, 170, 41, 31))
        self.label_day.setStyleSheet(u"font: 25 16pt \"Segoe UI Light\";\n"
                                     "color: rgb(255, 255, 255);")
        self.frame_employees = QFrame(self.frame)
        self.frame_employees.setObjectName(u"frame_employees")
        self.frame_employees.setGeometry(QRect(10, 430, 231, 361))
        self.frame_employees.setFrameShape(QFrame.StyledPanel)
        self.frame_employees.setFrameShadow(QFrame.Raised)
        #         self.frame_eployee = QFrame(self.frame_employees)
        #         self.frame_eployee.setObjectName(u"frame_eployee")
        #         self.frame_eployee.setGeometry(QRect(-10, 20, 241, 39))
        #         self.frame_eployee.setStyleSheet(u"color:rgb(85, 170, 255)")
        #         self.frame_eployee.setFrameShape(QFrame.StyledPanel)
        #         self.frame_eployee.setFrameShadow(QFrame.Raised)
        #         self.label_fix_logo_user = QLabel(self.frame_eployee)
        #         self.label_fix_logo_user.setObjectName(u"label_fix_logo_user")
        #         self.label_fix_logo_user.setGeometry(QRect(10, 10, 21, 16))
        #         self.label_fix_logo_user.setStyleSheet(u"background-image: url(:/user.png);")
        #         self.label_fix_logo_user.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/user.svg"))
        #         self.label_name_employee = QLabel(self.frame_eployee)
        #         self.label_name_employee.setObjectName(u"label_name_employee")
        #         self.label_name_employee.setGeometry(QRect(40, 10, 101, 21))
        #         self.label_name_employee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        # "font: 25 8pt \"Segoe UI Light\";")
        #         self.label_tim_login = QLabel(self.frame_eployee)
        #         self.label_tim_login.setObjectName(u"label_tim_login")
        #         self.label_tim_login.setGeometry(QRect(140, 10, 41, 21))
        #         self.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        # "font: 25 8pt \"Segoe UI Light\";")
        #         self.label_time_logOut = QLabel(self.frame_eployee)
        #         self.label_time_logOut.setObjectName(u"label_time_logOut")
        #         self.label_time_logOut.setGeometry(QRect(190, 10, 41, 21))
        #         self.label_time_logOut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        # "font: 25 8pt \"Segoe UI Light\";")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1149, 10, 121, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_wifi = QLabel(self.frame_2)
        self.label_wifi.setObjectName(u"label_wifi")
        self.label_wifi.setPixmap(QPixmap(u":/wifi.png"))

        self.horizontalLayout.addWidget(self.label_wifi)

        self.pushButton_setting = QPushButton(self.frame_2)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setStyleSheet(u"\n"
                                              "border-radius: 100px;")
        icon3 = QIcon()
        icon3.addFile(u":/Settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setting.setIcon(icon3)
        self.pushButton_setting.setIconSize(QSize(70, 70))

        self.horizontalLayout.addWidget(self.pushButton_setting)

        self.pushButton_setting.raise_()
        self.label_wifi.raise_()
        self.frame_T = QFrame(self.frame)
        self.frame_T.setObjectName(u"frame_T")
        self.frame_T.setGeometry(QRect(1050, 380, 180, 180))
        self.frame_T.setStyleSheet(u"background-color: rgba(84, 88, 92,120);\n"
                                   "border-radius:90px;\n"
                                   "")
        self.frame_T.setFrameShape(QFrame.NoFrame)
        self.frame_T.setFrameShadow(QFrame.Raised)
        self.circularProgressT = QFrame(self.frame_T)
        self.circularProgressT.setObjectName(u"circularProgressT")
        self.circularProgressT.setGeometry(QRect(0, 0, 180, 180))
        self.circularProgressT.setStyleSheet(u"border-radius:90px;\n"
                                             "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 85, 255, 0), stop:0.75 rgba(253, 54, 11, 80));\n"
                                             "\n"
                                             "")
        self.circularProgressT.setFrameShape(QFrame.NoFrame)
        self.circularProgressT.setFrameShadow(QFrame.Raised)
        self.containerT = QFrame(self.circularProgressT)
        self.containerT.setObjectName(u"containerT")
        self.containerT.setGeometry(QRect(15, 15, 150, 150))
        self.containerT.setStyleSheet(u"QFrame{\n"
                                      "background-color: rgb(29, 45, 53);\n"
                                      "border-radius:75px;\n"
                                      "}")
        self.containerT.setFrameShape(QFrame.StyledPanel)
        self.containerT.setFrameShadow(QFrame.Raised)
        self.label_temperature = QLabel(self.containerT)
        self.label_temperature.setObjectName(u"label_temperature")
        self.label_temperature.setGeometry(QRect(50, 40, 41, 51))
        self.label_temperature.setStyleSheet(u"color: rgb(234, 234, 235);\n"
                                             "font: 25 25pt \"Segoe UI Light\";")
        self.label_fix_logo_temperature = QLabel(self.containerT)
        self.label_fix_logo_temperature.setObjectName(u"label_fix_logo_temperature")
        self.label_fix_logo_temperature.setGeometry(QRect(30, 50, 21, 41))
        self.label_fix_logo_temperature.setBaseSize(QSize(10, 10))
        self.label_fix_logo_temperature.setPixmap(QPixmap(u":/temp.svg"))
        self.label_fix_logo_degree = QLabel(self.containerT)
        self.label_fix_logo_degree.setObjectName(u"label_fix_logo_degree")
        self.label_fix_logo_degree.setGeometry(QRect(100, 40, 31, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Light")
        font3.setPointSize(10)
        self.label_fix_logo_degree.setFont(font3)
        self.label_fix_temperature = QLabel(self.containerT)
        self.label_fix_temperature.setObjectName(u"label_fix_temperature")
        self.label_fix_temperature.setGeometry(QRect(20, 100, 101, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Light")
        font4.setPointSize(9)
        self.label_fix_temperature.setFont(font4)
        self.frame_H = QFrame(self.frame)
        self.frame_H.setObjectName(u"frame_H")
        self.frame_H.setGeometry(QRect(830, 380, 180, 180))
        self.frame_H.setStyleSheet(u"background-color: rgba(84, 88, 92,120);\n"
                                   "border-radius:90px;\n"
                                   "")
        self.frame_H.setFrameShape(QFrame.NoFrame)
        self.frame_H.setFrameShadow(QFrame.Raised)
        self.circularProgressH = QFrame(self.frame_H)
        self.circularProgressH.setObjectName(u"circularProgressH")
        self.circularProgressH.setGeometry(QRect(0, 0, 180, 180))
        self.circularProgressH.setStyleSheet(u"border-radius:90px;\n"
                                             "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 85, 255, 0), stop:0.75 rgba(115, 161, 206, 255));\n"
                                             "\n"
                                             "")
        self.circularProgressH.setFrameShape(QFrame.NoFrame)
        self.circularProgressH.setFrameShadow(QFrame.Raised)
        self.containerH = QFrame(self.circularProgressH)
        self.containerH.setObjectName(u"containerH")
        self.containerH.setGeometry(QRect(15, 15, 150, 150))
        self.containerH.setStyleSheet(u"QFrame{\n"
                                      "background-color: rgb(29, 45, 53);\n"
                                      "border-radius:75px;\n"
                                      "}")
        self.containerH.setFrameShape(QFrame.StyledPanel)
        self.containerH.setFrameShadow(QFrame.Raised)
        self.label_humidity = QLabel(self.containerH)
        self.label_humidity.setObjectName(u"label_humidity")
        self.label_humidity.setGeometry(QRect(50, 40, 41, 51))
        self.label_humidity.setStyleSheet(u"color: rgb(234, 234, 235);\n"
                                          "font: 25 25pt \"Segoe UI Light\";")
        self.label_fix_logo_humidity = QLabel(self.containerH)
        self.label_fix_logo_humidity.setObjectName(u"label_fix_logo_humidity")
        self.label_fix_logo_humidity.setGeometry(QRect(20, 50, 31, 41))
        self.label_fix_logo_humidity.setBaseSize(QSize(10, 10))
        self.label_fix_logo_humidity.setPixmap(QPixmap(u":/hum.svg"))
        self.label_fix_persent = QLabel(self.containerH)
        self.label_fix_persent.setObjectName(u"label_fix_persent")
        self.label_fix_persent.setGeometry(QRect(100, 40, 31, 21))
        self.label_fix_persent.setFont(font3)
        self.label_fix_persent.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_fix_humidity = QLabel(self.containerH)
        self.label_fix_humidity.setObjectName(u"label_fix_humidity")
        self.label_fix_humidity.setGeometry(QRect(20, 100, 101, 21))
        self.label_fix_humidity.setFont(font4)
        self.label_sayGood = QLabel(self.frame)
        self.label_sayGood.setObjectName(u"label_sayGood")
        self.label_sayGood.setGeometry(QRect(890, 590, 281, 101))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Light")
        font5.setPointSize(24)
        self.label_sayGood.setFont(font5)
        self.label_sayGood.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.verticalLayout = QVBoxLayout(self.frame_employees)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_lamp1.setText("")
        self.button_lamp2.setText("")
        self.button_lamp3.setText("")
        self.button_lamp4.setText("")
        self.label_lamp1.setText(QCoreApplication.translate("MainWindow", u"lamp1", None))
        self.label_lamp2.setText(QCoreApplication.translate("MainWindow", u"lamp2", None))
        self.label_lamp3.setText(QCoreApplication.translate("MainWindow", u"lamp3", None))
        self.label_lamp4.setText(QCoreApplication.translate("MainWindow", u"lamp4", None))
        self.button_lamp5.setText("")
        self.button_lamp6.setText("")
        self.button_lamp7.setText("")
        self.button_lamp8.setText("")
        self.label_lamp5.setText(QCoreApplication.translate("MainWindow", u"lamp5", None))
        self.label_lamp6.setText(QCoreApplication.translate("MainWindow", u"lamp6", None))
        self.label_lamp7.setText(QCoreApplication.translate("MainWindow", u"lamp7", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"lamp8", None))
        self.button_power.setText("")
        self.label_FixText.setText(QCoreApplication.translate("MainWindow", u"All of points", None))
        self.label_power.setText(QCoreApplication.translate("MainWindow", u"Turn off", None))
        self.button_door.setText("")
        self.label_fix_opendoor.setText(QCoreApplication.translate("MainWindow",
                                                                   u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#e6e6e6;\">Tap to open the door</span></p></body></html>",
                                                                   None))
        self.label_hour.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_minute.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"07", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"1400", None))
        self.label_day.setText(QCoreApplication.translate("MainWindow", u"04", None))
        # self.label_fix_logo_user.setText("")
        # self.label_name_employee.setText(QCoreApplication.translate("MainWindow", u"Arash Golsaz", None))
        # self.label_tim_login.setText(QCoreApplication.translate("MainWindow", u"08:34", None))
        # self.label_time_logOut.setText(QCoreApplication.translate("MainWindow", u"08:34", None))
        self.label_wifi.setText("")
        self.pushButton_setting.setText("")
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_fix_logo_temperature.setText("")
        self.label_fix_logo_degree.setText(QCoreApplication.translate("MainWindow",
                                                                      u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI Light'; font-size:10pt; color:#969696;\">\u00b0C</span></p></body></html>",
                                                                      None))
        self.label_fix_temperature.setText(QCoreApplication.translate("MainWindow",
                                                                      u"<html><head/><body><p align=\"center\"><span style=\" color:#ddddde;\">Temperature</span></p></body></html>",
                                                                      None))
        self.label_humidity.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_fix_logo_humidity.setText("")
        self.label_fix_persent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_fix_humidity.setText(QCoreApplication.translate("MainWindow",
                                                                   u"<html><head/><body><p align=\"center\"><span style=\" color:#ddddde;\">Humidity</span></p></body></html>",
                                                                   None))
        self.label_sayGood.setText(QCoreApplication.translate("MainWindow", u" Good morning", None))

    # retranslateUi

    def change_icon_lamp(self):
        # global icon_light_on, icon_light_off
        self.icon_light_on = QIcon()
        self.icon_light_off = QIcon()

        self.icon_light_on.addFile(u":/btn_on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_light_off.addFile(u":/btn_off.png", QSize(),
                                    QIcon.Normal,
                                    QIcon.Off)

    def change_icon_power(self, temp):
        # global icon_light_on, icon_light_off
        icon_power = QIcon()
        if temp == 0:
            icon_power.addFile(u":/btn_power_on.png", QSize(), QIcon.Normal, QIcon.Off)
            self.button_power.setIcon(icon_power)
        else:
            icon_power.addFile(u":/Dry_power.png", QSize(), QIcon.Normal, QIcon.Off)
            self.button_power.setIcon(icon_power)


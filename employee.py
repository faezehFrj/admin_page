from PySide2.QtCore import QCoreApplication,QRect
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *


class Person():
    def __init__(self, name, frame_employees):
        self.name = name
        self.frame_employees = frame_employees

    def config(self):
        self.frame_eployee = QFrame(self.frame_employees)
        self.frame_eployee.setObjectName(u"frame_eployee")
        self.frame_eployee.setStyleSheet(u"color:rgb(85, 170, 255)")
        self.frame_eployee.setFrameShape(QFrame.StyledPanel)
        self.frame_eployee.setFrameShadow(QFrame.Raised)
        self.label_fix_logo_user = QLabel(self.frame_eployee)
        self.label_fix_logo_user.setObjectName(u"label_fix_logo_user")
        self.label_fix_logo_user.setGeometry(QRect(10, 0, 41, 41))
        self.label_fix_logo_user.setPixmap(QPixmap(u"D:/V2.0.0/Programme/qt/UI design/picture/user.svg"))
        self.label_name_employee = QLabel(self.frame_eployee)
        self.label_name_employee.setObjectName(u"label_name_employee")
        self.label_name_employee.setGeometry(QRect(60, 10, 101, 21))
        self.label_name_employee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "font: 25 10pt \"Segoe UI Light\";")
        self.label_tim_login = QLabel(self.frame_eployee)
        self.label_tim_login.setObjectName(u"label_tim_login")
        self.label_tim_login.setGeometry(QRect(200, 10, 41, 21))
        self.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "font: 25 10pt \"Segoe UI Light\";")
        self.label_time_logOut = QLabel(self.frame_eployee)
        self.label_time_logOut.setObjectName(u"label_time_logOut")
        self.label_time_logOut.setGeometry(QRect(260, 10, 51, 21))
        self.label_time_logOut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                             "font: 25 10pt \"Segoe UI Light\";")

        self.label_fix_logo_user.setText("")
        self.label_name_employee.setText(QCoreApplication.translate("MainWindow", self.name, None))
        self.label_tim_login.setText(QCoreApplication.translate("MainWindow", u"08:00", None))
        self.label_time_logOut.setText(QCoreApplication.translate("MainWindow", u"08:00", None))

        return self.frame_eployee







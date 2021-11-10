import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtCore import QTimer, QDateTime
from PySide2.QtWidgets import *
# from uiDesignQT import Ui_MainWindow
from uiDashboardResize import Ui_MainWindow
from datetime import datetime
from employee import Person
import DataBase as db
import pickle
from ui_adminPage import Ui_MainWindowAdmin
from uiAlarmSave import Ui_MainWindow_alarm_save
import jdatetime
from uiCreateExport import Ui_MainCreateExport
from exportToExcel import ExportToExcel
from uiFingerprintPage import Ui_MainWindowFingerprint
from uiPassword import  Ui_MainWindowPassword
from uiDeleteEmployee import Ui_MainWindowDeleteAlarm


# import Mqtt

# ----------------admin____________________________

class MainWindowAdmin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_admin = Ui_MainWindowAdmin()
        self.ui_admin.setupUi(self)
        self.number_id_fingerprint_save = 0
        self.enroll_id_fingerprint = 0
        self.id_fingerprint_for_delete1=0
        self.id_fingerprint_for_delete2=0

        # show hours and data
        self.ui_admin.fram_after_add.hide()
        self.ui_admin.frame_features_one_employee.hide()
        self.ui_admin.fram_finish_employee.hide()
        self.setWindowFlag(Qt.FramelessWindowHint)

        # reade all employee from db
        self.epmloyees = db.main_select_all_employee()

        if len(self.epmloyees) < 8 and len(self.epmloyees) != 0:
            self.ui_admin.fram_after_add.show()

        elif len(self.epmloyees) == 0:
            self.ui_admin.label_6.hide()
            self.ui_admin.label_text_first_2.hide()
            self.ui_admin.fram_after_add.show()

        elif len(self.epmloyees) == 8:
            self.ui_admin.fram_finish_employee.show()

        # show button employee
        self.show_button_employee()

        # id employee select shode
        self.id_employee_select = 0

        self.ui_admin.employee1.clicked.connect(lambda: self.show_features_employee(0))
        self.ui_admin.employee2.clicked.connect(lambda: self.show_features_employee(1))
        self.ui_admin.employee3.clicked.connect(lambda: self.show_features_employee(2))
        self.ui_admin.employee4.clicked.connect(lambda: self.show_features_employee(3))
        self.ui_admin.employee5.clicked.connect(lambda: self.show_features_employee(4))
        self.ui_admin.employee6.clicked.connect(lambda: self.show_features_employee(5))
        self.ui_admin.employee7.clicked.connect(lambda: self.show_features_employee(6))
        self.ui_admin.employee8.clicked.connect(lambda: self.show_features_employee(7))

        # self.ui_admin.checkBox_active.stateChanged.connect(lambda: self.change())

        # self.ui_admin.delete_employee.clicked.connect(self.delete_employee_select)


    #---------delete employee---------------

    def delete_employee_select(self):

        db.delete_employee(self.id_employee_select)
        # hide_frams
        for i in range(8):
            print(i)
            self.frams[i].hide()
        self.show_button_employee()
        self.ui_admin.frame_features_one_employee.hide()
        self.ui_admin.fram_after_add.show()







    def change(self):

        if self.ui_admin.checkBox_active.isChecked()==True:
            db.update_status_employee("0",self.id_employee_select)
            self.ui_admin.label_activeOrDi.setText("diactive")
            self.ui_admin.label_activeOrDi.setStyleSheet(u"color: rgb(127, 132, 137);")
            print("diactive")
        else:
            print("active")
            db.update_status_employee("1", self.id_employee_select)
            self.ui_admin.label_activeOrDi.setText("active")
            self.ui_admin.label_activeOrDi.setStyleSheet(u"color: rgb(0, 173, 239);")

        self.update_list_employee()


    def show_features_employee(self, id_employee_choose):

        #---------set id fram -----

        self.id_employee_for_delete=id_employee_choose
        #print(id_employee_choose)
        self.ui_admin.fram_after_add.hide()
        self.ui_admin.delete_employee.show()
        self.ui_admin.frame_features_one_employee.show()
        name = self.epmloyees[id_employee_choose][2]
        family = self.epmloyees[id_employee_choose][3]
        rfid = self.epmloyees[id_employee_choose][1]
        self.id_fingerprint_for_delete1 = self.epmloyees[id_employee_choose][4]
        self.id_fingerprint_for_delete2 = self.epmloyees[id_employee_choose][5]
        self.ui_admin.lineEdit_fname.setText(QCoreApplication.translate("MainWindow", name, None))
        self.ui_admin.lineEdit_Lname.setText(QCoreApplication.translate("MainWindow", family, None))
        self.ui_admin.label_RFID.setText(QCoreApplication.translate("MainWindow", rfid, None))
        self.ui_admin.label_t_name.setText(name)
        self.ui_admin.label_2.setText("Features")
        self.ui_admin.pushButton_export.show()
        self.ui_admin.checkBox_active.show()
        self.ui_admin.label_activeOrDi.show()
        self.ui_admin.pushButton_save_finger.show()

        # show alarm bellow finger print
        if self.epmloyees[id_employee_choose][6] == "0":
            self.ui_admin.label_message_number_fingerprint.setText("add your frist fingerprint")
            self.ui_admin.label_id_fingerprint.setText(self.epmloyees[id_employee_choose][4])
            self.enroll_id_fingerprint = self.epmloyees[id_employee_choose][4]
        elif self.epmloyees[id_employee_choose][6] == "1":
            self.ui_admin.label_message_number_fingerprint.setText("one fingerprint has saved")
            self.ui_admin.label_id_fingerprint.setText(self.epmloyees[id_employee_choose][5])
            self.enroll_id_fingerprint = self.epmloyees[id_employee_choose][5]
        else:
            self.ui_admin.label_message_number_fingerprint.setText("fingerprint has saved")
            self.ui_admin.label_id_fingerprint.setText(self.epmloyees[id_employee_choose][5])
        temp = self.epmloyees[id_employee_choose][0]
        self.set_id(temp)
        self.set_rfid_select_employee(self.epmloyees[id_employee_choose][1])
        self.number_id_fingerprint_save = self.epmloyees[id_employee_choose][6]
        # self.ui_admin.label_message_number_fingerprint.setText(self.epmloyees[id_employee_choose][4])


        #show acitive and diactive
        if self.epmloyees[id_employee_choose][7] == "1":
            self.ui_admin.checkBox_active.setChecked(False)
        else:
            self.ui_admin.checkBox_active.setChecked(True)

    ####show employeee
    def show_button_employee(self):

        self.show_detail_employee = []
        self.frams = self.ui_admin.add_framEmployee_array()
        epmloyees = db.main_select_all_employee()


        for j in range(len(epmloyees)):
            array = []
            self.frams[j].show()
            temp = epmloyees[j][2] + "\n" + epmloyees[j][3]
            self.frams[j].setText(temp)
            array.append(epmloyees[j][0])
            array.append(self.frams[j])
            self.show_detail_employee.append(array)

    def set_id(self, id_person):
        self.id_employee_select = id_person

    def get_id(self):
        return self.id_employee_select

    def update_list_employee(self):
        self.epmloyees = db.main_select_all_employee()

    def get_epmloyees(self):
        return self.epmloyees

    def get_rfid_select_employee(self):
        return self.frid_employee_select

    def set_rfid_select_employee(self, rfid_select):
        self.frid_employee_select = rfid_select

    def get_number_employee(self):
        return len(self.epmloyees)

    # ---for save fingerpring-----

    # ---update number fingerprint save after add fingerprint in device

    def update_number_fingerprint_define(self):
        db.update_number_status_finger(self.id_employee_select, str(int(self.number_id_fingerprint_save) + 1))


# -------------fingerprint------------------

class MainWindowFingerprint(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_finger = Ui_MainWindowFingerprint()
        self.ui_finger.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)


# ------------------------------------------
class MainCreateExport(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_export = Ui_MainCreateExport()
        self.ui_export.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui_export.comboBox.currentTextChanged.connect(self.combo_selected)
        self.UiComponents()
        # connected combobox signal

    def UiComponents(self):
        # creating a check-able combo box object
        # self.combo_box =self.ui_export.comboBox

        # geek list
        geek_list = ["Farvardin", "Ordibehesht", "khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey",
                     "Bahman", "Esfand"]

        # adding list of items to combo box
        self.ui_export.comboBox.addItems(geek_list)

        # setting style sheet
        # adding border to down arrow
        # setting border style to it when it get pressed
        # self.combo_box.setStyleSheet("QComboBox::down-arrow"
        #                              "{"
        #                              "border : 2px solid black;"
        #                              "}"
        #                              "QComboBox::down-arrow:pressed"
        #                              "{"
        #                              "border-style : dotted;"
        #                              "}")'

    def combo_selected(self):
        self.item = self.ui_export.comboBox.currentText()

    def create_export(self, id):
        print(self.item)
        print(id)
        a = ExportToExcel(self.item, id)
        return a.create_in_file()


# ----------------------------------------
# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.records=[]
        self.setWindowFlag(Qt.FramelessWindowHint)
        # show hours and data
        self.timer = QTimer()
        self.timer.timeout.connect(self.showNowTime)
        self.tempratureBarValue(75)
        self.humidBarValue(56)

        # self.ui.button_lamp1.clicked.connect(self.the_button_was_clicked1)

        self.today = datetime.today().date()
        self.array_employee = []

    # show hours and data
    def showNowTime(self):

        time = QDateTime.currentDateTime()
        hourDisplay = time.toString('hh')
        minuteDisplay = time.toString('mm')
        # yearDisplay = time.toString('yyyy')
        # monthDisplay = time.toString('MM')
        # dayDisplay = time.toString('dd')
        yearDisplay = jdatetime.datetime.now().strftime("%Y")
        monthDisplay = jdatetime.datetime.now().strftime("%m")
        dayDisplay = jdatetime.datetime.now().strftime("%d")
        self.timer.start(1000)
        self.ui.label_minute.setText(QCoreApplication.translate("MainWindow", minuteDisplay, None))
        self.ui.label_hour.setText(QCoreApplication.translate("MainWindow", hourDisplay, None))
        self.ui.label_year.setText(QCoreApplication.translate("MainWindow", yearDisplay, None))
        self.ui.label_13.setText(QCoreApplication.translate("MainWindow", monthDisplay, None))
        self.ui.label_day.setText(QCoreApplication.translate("MainWindow", dayDisplay, None))


        if self.today < datetime.today().date():
            self.today = datetime.today().date()

        if hourDisplay == "00":
            for person in self.array_employee:

                person[1].label_tim_login.setStyleSheet(u"color: rgb(127, 132, 137);\n"
                                                "font: 25 9pt \"Segoe UI Light\";")
                person[1].label_time_logOut.setStyleSheet(u"color: rgb(127, 132, 137);\n"
                                                    "font: 25 9pt \"Segoe UI Light\";")
                person[1].label_name_employee.setStyleSheet(u"color:  rgb(127, 132, 137);\n"
                                                    "font: 25 9pt \"Segoe UI Light\";")
                person[1].label_tim_login.setText("--:--")
                person[1].label_time_logOut.setText("--:--")




    def the_button_was_clicked1(self):
        print("ddd")
        p = Person("faezeh farajzade", self.ui.frame_employees)
        self.ui.verticalLayout.addWidget(p.config())
        self.array_employee.append(p)


    # ----------show admin page---------------
    # def go_to_admin_page(self):
    #
    #     window = MainWindowAdmin()
    #     window.show()
    #     sys.exit(app.exec_())

    def show_employee(self):
        self.records = db.getAllEmployeeAndTime()

        for row in self.records:
            p = Person(row[1], self.ui.frame_employees)
            temp_array = []
            self.ui.verticalLayout.addWidget(p.config())
            temp_array.append(row[0])
            temp_array.append(p)
            self.array_employee.append(temp_array)

            #new add show last status

            time=db.selectEmployeeAndTimeIN(row[2])
            if len(time)!=0:
                p.label_tim_login.setText(time[0][0])
                p.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "font: 25 9pt \"Segoe UI Light\";")
                p.label_name_employee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "font: 25 9pt \"Segoe UI Light\";")
                if time[0][1]!="":
                    p.label_time_logOut.setText(time[0][1])
                    p.label_tim_login.setStyleSheet(u"color: rgb(127, 132, 137);\n"
                                                    "font: 25 9pt \"Segoe UI Light\";")
                    p.label_name_employee.setStyleSheet(u"color:  rgb(127, 132, 137);\n"
                                                        "font: 25 9pt \"Segoe UI Light\";")


        # for row in range(len(self.array_employee)):
        #     print(self.array_employee[row][1])


    def get_list_employee(self):
        return self.array_employee

    def test(self):

        array = self.get_list_employee()
        for rows in range(len(array)):

            if 1 == array[rows][0]:
                person = array[rows][1]
                person.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 12);\n"
                                                     "font: 25 8pt \"Segoe UI Light\";")
                break

    def change_color_form_employee(self):

        self.ui.label_name_employee.setStyleSheet(u"color: rgb(124, 124, 124);\n"
                                                  "font: 25 8pt \"Segoe UI Light\";")
        self.ui.label_time.setStyleSheet(u"color: rgb(124, 124, 124);\n"
                                         "font: 25 8pt \"Segoe UI Light\";")

    def tempratureBarValue(self, value):

        styleSheet = """
            border-radius:90px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop: {stop_1} rgba(255, 85, 255, 0), stop: {stop_2} rgba(253, 54, 11, 80));
        """



        progress = (100 - value) / 100.0

        # get new value
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # replace
        styleSheetNew = styleSheet.replace("{stop_1}", stop_1).replace("{stop_2}", stop_2)

        # set new stylesheet
        self.ui.label_temperature.setText(QCoreApplication.translate("MainWindow", str(value), None))
        self.ui.circularProgressT.setStyleSheet(styleSheetNew)

    def humidBarValue(self, value):

        styleSheet = """
         border-radius:90px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 85, 255, 0), stop:{STOP_2} rgba(115, 161, 206, 255));

        """

        progress = (100 - value) / 100.0

        # get new value
        temp=progress - 0.001
        stop_1 = str(int(temp))
        stop_2 = str(int(progress))

        # replace
        styleSheetNew = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # set new stylesheet

        self.ui.circularProgressH.setStyleSheet(styleSheetNew)

        self.ui.label_humidity.setText(QCoreApplication.translate("MainWindow", str(value), None))




class AlarmSaveEmployee(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_alarm_save = Ui_MainWindow_alarm_save()
        self.ui_alarm_save.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)


class PasswordCheck(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_pass = Ui_MainWindowPassword()
        self.ui_pass.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

class DeleteEmployee(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_delete = Ui_MainWindowDeleteAlarm()
        self.ui_delete.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)






if __name__ == "__main__":
    # Mqtt.configmqtt()
    app = QApplication(sys.argv)
    # window = MainWindow()
    # window.showNowTime()
    # window.show_employee()
    # window.test()
    window = MainCreateExport()
    window.show()
    #
    #     window=MainWindowAdmin()
    #     window.show_button_employee()
    #     window.show()
    sys.exit(app.exec_())

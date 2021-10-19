import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtCore import QTimer, QDateTime
from PySide2.QtWidgets import *
from uiDesignQT import Ui_MainWindow
from datetime import datetime
from employee import Person
import DataBase as db
import pickle
from ui_adminPage import Ui_MainWindowAdmin
from uiAlarmSave import Ui_MainWindow_alarm_save
# import Mqtt

#----------------admin____________________________

class MainWindowAdmin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_admin = Ui_MainWindowAdmin()
        self.ui_admin.setupUi(self)
        # show hours and data
        self.ui_admin.fram_after_add.hide()
        self.ui_admin.frame_features_one_employee.hide()
        self.ui_admin.fram_finish_employee.hide()
        self.setWindowFlag(Qt.FramelessWindowHint)

        #reade all employee from db
        self.epmloyees = db.main_select_all_employee()

        if len(self.epmloyees)<8 and len(self.epmloyees)!=0:
            self.ui_admin.fram_after_add.show()

        elif len(self.epmloyees)==0:
            self.ui_admin.label_6.hide()
            self.ui_admin.label_text_first_2.hide()
            self.ui_admin.fram_after_add.show()

        elif len(self.epmloyees)==8:
            self.ui_admin.fram_finish_employee.show()

        #show button employee
        self.show_button_employee()

        #id employee select shode
        self.id_employee_select=0

        self.ui_admin.employee1.clicked.connect(lambda: self.show_features_employee(0))
        self.ui_admin.employee2.clicked.connect(lambda: self.show_features_employee(1))
        self.ui_admin.employee3.clicked.connect(lambda: self.show_features_employee(2))
        self.ui_admin.employee4.clicked.connect(lambda: self.show_features_employee(3))
        self.ui_admin.employee5.clicked.connect(lambda: self.show_features_employee(4))
        self.ui_admin.employee6.clicked.connect(lambda: self.show_features_employee(5))
        self.ui_admin.employee7.clicked.connect(lambda: self.show_features_employee(6))
        self.ui_admin.employee8.clicked.connect(lambda: self.show_features_employee(7))




    def show_features_employee(self,id_employee_choose):
        #print(id_employee_choose)
        self.ui_admin.fram_after_add.hide()
        self.ui_admin.frame_features_one_employee.show()
        name = self.epmloyees[id_employee_choose][2]
        family = self.epmloyees[id_employee_choose][3]
        rfid = self.epmloyees[id_employee_choose][1]
        self.ui_admin.lineEdit_fname.setText(QCoreApplication.translate("MainWindow",name , None))
        self.ui_admin.lineEdit_Lname.setText(QCoreApplication.translate("MainWindow", family, None))
        self.ui_admin.label_RFID.setText(QCoreApplication.translate("MainWindow", rfid, None))
        self.ui_admin.label_t_name.setText(name)
        self.ui_admin.label_2.setText("Features")

        #show alarm bellow finger print
        if self.epmloyees[id_employee_choose][6]=="0":
            self.ui_admin.label_message_number_fingerprint.setText("add your frist fingerprint")
            self.ui_admin.label_id_fingerprint.setText(self.epmloyees[id_employee_choose][4])
        elif self.epmloyees[id_employee_choose][6]=="1":
            self.ui_admin.label_message_number_fingerprint.setText("one fingerprint has saved")
            self.ui_admin.label_id_fingerprint.setText(self.epmloyees[id_employee_choose][5])
        else:
            self.ui_admin.label_message_number_fingerprint.setText("fingerprint has saved")
        self.set_id(self.epmloyees[id_employee_choose][0])
        self.set_rfid_select_employee(self.epmloyees[id_employee_choose][1])
        #self.ui_admin.label_message_number_fingerprint.setText(self.epmloyees[id_employee_choose][4])


    ####show employeee
    def show_button_employee(self):
        self.show_detail_employee = []
        frams=self.ui_admin.add_framEmployee_array()
        epmloyees = db.main_select_all_employee()
        # for i in a:
        #     print(i)
        # a[1].show()
        for j in range(len(epmloyees)):
            array=[]
            frams[j].show()
            temp=epmloyees[j][2]+"\n"+epmloyees[j][3]
            frams[j].setText(temp)
            array.append(epmloyees[j][0])
            array.append(frams[j])
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
        self.frid_employee_select=rfid_select

    def get_number_employee(self):
        return len(self.epmloyees)


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # show hours and data
        self.timer = QTimer()
        self.timer.timeout.connect(self.showNowTime)
        self.tempratureBarValue(75)
        self.humidBarValue(56)

        #self.ui.button_lamp1.clicked.connect(self.the_button_was_clicked1)


        self.today = datetime.today().date()
        self.array_employee = []
    # show hours and data
    def showNowTime(self):
        time = QDateTime.currentDateTime()
        hourDisplay = time.toString('hh')
        minuteDisplay = time.toString('mm')
        yearDisplay = time.toString('yyyy')
        monthDisplay = time.toString('MM')
        dayDisplay = time.toString('dd')
        self.timer.start(1000)
        self.ui.label_minute.setText(QCoreApplication.translate("MainWindow", minuteDisplay, None))
        self.ui.label_hour.setText(QCoreApplication.translate("MainWindow", hourDisplay, None))
        self.ui.label_year.setText(QCoreApplication.translate("MainWindow", yearDisplay, None))
        self.ui.label_3.setText(QCoreApplication.translate("MainWindow", monthDisplay, None))
        self.ui.label_day.setText(QCoreApplication.translate("MainWindow", dayDisplay, None))


        if self.today < datetime.today().date():
            self.today = datetime.today().date()


    def the_button_was_clicked1(self):
        print("ddd")
        p = Person("faezeh farajzade", self.ui.frame_employees)
        self.ui.verticalLayout.addWidget(p.config())
        self.array_employee.append(p)

    #----------show admin page---------------
    # def go_to_admin_page(self):
    #
    #     window = MainWindowAdmin()
    #     window.show()
    #     sys.exit(app.exec_())


    def show_employee(self):
        records=db.getAllEmployeeAndTime()

        for row in records:
            p = Person(row[1], self.ui.frame_employees)
            temp_array=[]
            self.ui.verticalLayout.addWidget(p.config())
            temp_array.append(row[0])
            temp_array.append(p)
            self.array_employee.append(temp_array)


        for row in range(len(self.array_employee)):
              print(self.array_employee[row][0])


    def get_list_employee(self):
        return self.array_employee

    def test(self):

        array = self.get_list_employee()
        for rows in range(len(array)):

            if 1 == array[rows][0]:
                person = array[rows][1]
                person.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 12);\n"
                                               "font: 25 10pt \"Segoe UI Light\";")
                break


    def change_color_form_employee(self):

        self.ui.label_name_employee.setStyleSheet(u"color: rgb(124, 124, 124);\n"
                                                  "font: 25 10pt \"Segoe UI Light\";")
        self.ui.label_time.setStyleSheet(u"color: rgb(124, 124, 124);\n"
                                         "font: 25 10pt \"Segoe UI Light\";")

    def tempratureBarValue(self,value):

        styleSheet="""
            border-radius:115px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop_1} rgba(255, 85, 255, 0), stop:{stop_2} rgba(253, 54, 11, 80));
        """

        progress=(100-value)/100.0

        #get new value
        stop_1=str(progress-0.001)
        stop_2=str(progress)

        #replace
        styleSheetNew=styleSheet.replace("{stop_1}",stop_1).replace("{stop_2}",stop_2)

        #set new stylesheet
        self.ui.label_temperature.setText(QCoreApplication.translate("MainWindow", str(value), None))
        self.ui.circularProgressT.setStyleSheet(styleSheetNew)




    def humidBarValue(self,value):

        styleSheet="""
            border-radius:115px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 85, 255, 0), stop:{STOP_2} rgba(115, 161, 206, 255));
        """

        progress=(100-value)/100.0

        #get new value
        stop_1=str(progress-0.001)
        stop_2=str(progress)

        #replace
        styleSheetNew=styleSheet.replace("{STOP_1}",stop_1).replace("{STOP_2}",stop_2)

        #set new stylesheet

        self.ui.circularProgressH.setStyleSheet(styleSheetNew)

        self.ui.label_humidity.setText(QCoreApplication.translate("MainWindow", str(value), None))

class AlarmSaveEmployee(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_alarm_save = Ui_MainWindow_alarm_save()
        self.ui_alarm_save.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)



# if __name__ == "__main__":
#    # Mqtt.configmqtt()
#     app = QApplication(sys.argv)
#     # window = MainWindow()
#     # window.showNowTime()
#     # window.show_employee()
#     # window.test()
#
#     window=MainWindowAdmin()
#     window.show_button_employee()
#     window.show()
#     sys.exit(app.exec_())

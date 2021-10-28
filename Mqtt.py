import paho.mqtt.client as mqttClient
from datetime import datetime
import DataBase as db
import time
import threading
import main as ui
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, QCoreApplication
import jdatetime
from employee import Person as new_Person


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

Connected = False  # global variable for the state of the connection
broker_address = "127.0.0.1"  # Broker address
port = 1883  # Broker port
user = "yourUser"  # Connection username
password = "yourPassword"  # Connection password
myGlobalMessagePayload = ''  # HERE!
state_rfid = 0  # baraye in ke bebinim mikhad fard jadid  tarif kone ya in ke mikhad haminjor biyad to
id_rfid_employee = 0
buttonClicked = 0
status_crete_employee = 0
statusLamp = [0, 0, 0, 0, 0, 0, 0, 0,0]
app = ui.QApplication(ui.sys.argv)
window = ui.MainWindow()
windowadmin = ui.MainWindowAdmin()
windowAlarmEmployee = ui.AlarmSaveEmployee()
windowExport=ui.MainCreateExport()
windowFingerPrint=ui.MainWindowFingerprint()
windowPassword=ui.PasswordCheck()
windowDelete=ui.DeleteEmployee()
window.showNowTime()
window.show_employee()



def on_connect(self, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


def on_message(client, userdata, msg):
    # global message
    # message = msg.payload.decode()
    subscribe_all_topic(msg.topic, msg.payload.decode())
    # //
    # global myGlobalMessagePayload
    # if msg.topic == 'python/test':
    #     myGlobalMessagePayload = msg.payload.decode() # HERE!
    #     print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    # //
    # window.set_result_text(msg.payload.decode())

    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    # return msg.payload.decode()


def publish(client, m, topic_publish):
    msg_count = 0
    # while True:
    #     time.sleep(1)
    msg = f"messages: {msg_count}"
    result = client.publish(topic_publish, m)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{m}` to topic `{topic_publish}`")
    else:
        print(f"Failed to send message to topic {topic_publish}")
    msg_count += 1


def get_payload():
    return myGlobalMessagePayload


# app = ui.QApplication(ui.sys.argv)
# window = ui.MainWindow()
# ui.sys.exit(app.exec_())


#####subscribe######
def subscribe_all_topic(topic_subscrib, mesege):
    global buttonClicked, set_time, t
    set_time = setTimer(5)
    set_time.cancel()

    ####---------------------------rfid----------------------------------####
    if "publish/RFIDCode" == topic_subscrib:
        # publish(client, "state/buzzer/automatic", "state/buzzer")
        setIDrfid(mesege)  # add rfid code to id_rfid_employee variable
        resultDB = db.searchIdCard(mesege)
        print(resultDB)
        if not resultDB:
            publish(client, "state/openDoor/fail", "state")

        else:
            detrmineStatusButton(resultDB)

        # if status_crete_employee == 1:
        windowadmin.ui_admin.label_RFID.setText(id_rfid_employee)





    ####------------------------fingerprint------------------------------####

    # ******added new one *******#

    elif "enroll/getImage" == topic_subscrib:
        if "2" == mesege:
            print(".")
            windowFingerPrint.ui_finger.label_lavel.setStyleSheet(u"color: rgb(65, 187, 255);")
        else:
            windowFingerPrint.ui_finger.alarm.setText(mesege)

    elif "enroll/convertToTemplate" == topic_subscrib:

        exception = {
            "1": "Image converted",
            "2": "Image too messy",
            "3": "Communication error",
            "4": "Could not find fingerprint features",
            "5": "Could not find fingerprint features",
            "6": "Unknown error"
        }
        print(exception[mesege])
        windowFingerPrint.ui_finger.alarm.setText(exception[mesege])

    elif "enroll/RemoveFinger" == topic_subscrib:
        print(mesege)
        windowFingerPrint.ui_finger.alarm.setText(" ")
        windowFingerPrint.ui_finger.label_level2.styleSheet(u"color: rgb(65, 187, 255);")

    elif "enroll/getImage2" == topic_subscrib:
        if "2" == mesege:
            print(".")
            windowFingerPrint.ui_finger.label_lavel.setStyleSheet(u"color: rgb(65, 187, 255);")
        else:
            windowFingerPrint.ui_finger.alarm.setText(mesege)

    elif "enroll/store" == topic_subscrib:
        if "Stored!" == mesege:
            print(mesege)
            windowFingerPrint.ui_finger.alarm.setText("succssfully")
            windowFingerPrint.ui_finger.label_level4.styleSheet(u"color: rgb(65, 187, 255);")

        else:
            windowFingerPrint.ui_finger.alarm.setText(mesege)

    # *****find finger print ******#

    elif "search/find" == topic_subscrib:
        t.cancel()

        if "denied" == mesege:
            publish(client, "state/openDoor/fail", "state")
        else:
            resultDB = db.select_employee_by_fingerprint(mesege)
            detrmineStatusButton(resultDB)

    ####-----------------------touch button status--------------------------------#####

    if "button/click" == topic_subscrib:
        t = setTimer(10)

        if buttonClicked == 1:
            t.cancel()
            publish(client, "state/login", "state")
            buttonClicked = 2
            t.start()
        elif buttonClicked == 2:
            t.cancel()
            publish(client, "state/logout", "state")
            print("logout")
            buttonClicked = 0
            t.start()
        elif buttonClicked == 0:
            publish(client, "state/openDoor/show", "state")
            publish(client, "state/fingerprint/run", "state/fingerprint")
            buttonClicked = 1
            t.start()

    ####------------------------buzzer---------------------------------------------####

    ####-------------------------oled----------------------------------------------####

    ####------------------------ring button----------------------------------------#####
    ####------------------------timer --------------------------------------------####


# ********************************publish********************************************#

####rfid####

####fingerprint####

def createFingerprint(idEmployeeForFp):
    publish(client, idEmployeeForFp, "enroll/getId")
    publish(client, "state/openDoor/request", "state")


def stopFingerprint():
    publish(client, "enroll/program/stop", "enroll/program")
    publish(client, "state/normal", "state")


####buzzer####

####oled#####

####ring button#####

####touch button status#####


#####get and set #####

####rfid####
def getIDrfid():
    global id_rfid_employee
    return id_rfid_employee


def setIDrfid(idForSetRfid):
    global id_rfid_employee
    id_rfid_employee = idForSetRfid


# ******method******

def detrmineStatusButton(resultDB):
    global buttonClicked

    now = datetime.now()
    today = jdatetime.datetime.now().strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    print(buttonClicked)
    if buttonClicked == 1:
        publish(client, "", "open/door")
        publish(client, "state/openDoor/access", "state")


    # ****login****#
    elif buttonClicked == 2:
        ####save login in data base####
        db.mainCreateLog(today, current_time, '', resultDB[0][1])
        array = window.get_list_employee()
        for rows in range(len(array)):
            if resultDB[0][0] == array[rows][0]:
                person = array[rows][1]
                # break
                person.label_tim_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                     "font: 25 9pt \"Segoe UI Light\";")
                person.label_name_employee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                         "font: 25 9pt \"Segoe UI Light\";")
                person.label_tim_login.setText(current_time)
                print("click")
        ####set ui log in and log out
        # window.ui.

        #### show in oled ####

        publish(client, resultDB[0][2], "information/employee/name")
        publish(client, current_time, "information/employee/time")
        publish(client, "state/openDoor/ok", "state")




    # ****logout****#
    elif buttonClicked == 0:
        set_time.start()
        ####save logout in data base####
        db.updateLogTable(current_time, resultDB[0][1])
        ####show oled #####
        publish(client, resultDB[0][2], "information/employee/name")
        publish(client, current_time, "information/employee/time")
        publish(client, "state/openDoor/ok", "state")

        array = window.get_list_employee()
        for rows in range(len(array)):
            if resultDB[0][0] == array[rows][0]:
                person = array[rows][1]
                # break
                person.label_time_logOut.setStyleSheet(u"color: rgb(121, 121, 121);\n"
                                                       "font: 25 10pt \"Segoe UI Light\";")
                person.label_tim_login.setStyleSheet(u"color: rgb(121, 121, 121);\n"
                                                     "font: 25 10pt \"Segoe UI Light\";")
                person.label_name_employee.setStyleSheet(u"color: rgb(121, 121, 121);\n"
                                                         "font: 25 10pt \"Segoe UI Light\";")
                person.label_time_logOut.setText(current_time)


# ------------------normal status----------------#
def resetFactory():
    global buttonClicked
    publish(client, "state/normal", "state")
    publish(client, "state/fingerprint/stop", "state/fingerprint")
    buttonClicked = 0
    t.cancel()
    set_time.cancel()


# -----------------timer-----------------------#
def setTimer(second):
    reset_system = threading.Timer(second, resetFactory)
    return reset_system


def configmqtt():
    global client
    client = mqttClient.Client("Python")  # create new instance
    # client.username_pw_set(user, password=password)  # set username and password
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message  # attach function to callback

    client.connect(broker_address, port=port)  # connect to broker

    client.loop_start()  # start the loop
    client.subscribe("python/test")
    client.subscribe("publish/RFIDCode")
    client.subscribe("button/click")
    client.subscribe("enroll/getImage")
    client.subscribe("enroll/convertToTemplate")
    client.subscribe("enroll/RemoveFinger")
    client.subscribe("enroll/store")
    client.subscribe("search/find")

    # time.sleep(1)
    while Connected != True:  # Wait for connection
        time.sleep(0.1)
        print("waite for connected")

    # try:
    #         while True:
    #             time.sleep(1)
    #
    # except KeyboardInterrupt:
    #         print("exiting")
    #         client.disconnect()
    #         client.loop_stop()


def get_clientvalue():
    return client

#----action button----------
def function_button():
    window.ui.change_icon_lamp()
    window.ui.button_lamp1.clicked.connect(the_button_was_clicked1)
    window.ui.button_lamp2.clicked.connect(the_button_was_clicked2)
    window.ui.button_lamp3.clicked.connect(the_button_was_clicked3)
    window.ui.button_lamp4.clicked.connect(the_button_was_clicked4)
    window.ui.button_lamp5.clicked.connect(the_button_was_clicked5)
    window.ui.button_lamp6.clicked.connect(the_button_was_clicked6)
    window.ui.button_lamp7.clicked.connect(the_button_was_clicked7)
    window.ui.button_lamp8.clicked.connect(the_button_was_clicked8)
    window.ui.button_door.clicked.connect(the_button_door_clicked)
    window.ui.button_power.clicked.connect(access_all_button)
    # window.ui.pushButton_setting.clicked.connect(go_to_admin_page)
    window.ui.pushButton_setting.clicked.connect(go_to_varufy_password)
    windowadmin.ui_admin.pushButton_5.clicked.connect(create_new_employee)
    windowadmin.ui_admin.button_add_first.clicked.connect(create_new_employee)
    windowadmin.ui_admin.pushButton_save.clicked.connect(save_or_edit_employee)
    windowadmin.ui_admin.pushButton_Adashboard.clicked.connect(back_dashboard)
    windowadmin.ui_admin.pushButton_export.clicked.connect(show_export_page)
    windowadmin.ui_admin.pushButton_save_finger.clicked.connect(show_finger_print_page)
    windowAlarmEmployee.ui_alarm_save.pushButton_alarm_save.clicked.connect(close_save_window)
    windowExport.ui_export.pushButton_ok.clicked.connect(create_export)
    windowExport.ui_export.pushButton_close.clicked.connect(close_page_export)
    windowFingerPrint.ui_finger.pushButton_click.clicked.connect(close_page_fingerprint)
    #-----password

    windowPassword.ui_pass.pushButton_cancel_pass.clicked.connect(back_dashboard)
    windowPassword.ui_pass.pushButton_check_pass.clicked.connect(varify_password)

    #-----close project
    windowadmin.ui_admin.pushButton_Exit.clicked.connect(close_project)

    #----alarm delete employee-----
    windowadmin.ui_admin.delete_employee.clicked.connect(show_sure_delete)
    windowDelete.ui_delete.pushButton_okey_delete.clicked.connect(delete_employee)
    windowDelete.ui_delete.pushButton_okey_delete.clicked.connect(cancel_delete_employee)



#------delete employee--------
def show_sure_delete():
    windowadmin.ui_admin.blur(2)
    windowDelete.show()

def delete_employee():

    windowadmin.ui_admin.blur(0)
    windowDelete.hide()
    windowadmin.delete_employee_select()
    clearLayout(window.ui.frame_employees.layout())
    window.show_employee()

def clearLayout(layout):
  while layout.count():
    child = layout.takeAt(0)
    if child.widget():
      child.widget().deleteLater()


def cancel_delete_employee():
    windowadmin.ui_admin.blur(0)
    windowDelete.hide()
#---------close_project methode----------
def close_project():
    windowadmin.hide()


#-------------varify password--------

def go_to_varufy_password():
    windowPassword.show()
    window.ui.blur(2)

def varify_password():
    my_pass="1212"
    if windowPassword.ui_pass.lineEdit_password.text() == my_pass:
        go_to_admin_page()
        windowPassword.ui_pass.label_alarm_pass.setText("")
        windowPassword.ui_pass.lineEdit_password.setText("")
        windowPassword.hide()
    else:
        windowPassword.ui_pass.label_alarm_pass.setText("wrong! try again")
        windowPassword.ui_pass.lineEdit_password.setText("")




#-------------------export------------------------
def show_export_page():
    windowExport.ui_export.lable_result_export.setText(" ")
    windowExport.show()
    windowadmin.ui_admin.blur(2)


def close_page_export():
    windowExport.hide()
    windowadmin.ui_admin.blur(0)


def create_export():
    result=windowExport.create_export(windowadmin.id_employee_select)
    if result==True:
        windowExport.ui_export.lable_result_export.setText("export successful")
    else:
        windowExport.ui_export.lable_result_export.setText("There isn't any data")

#---------------export---------------------------



#---------------fingerprint----------------------
def show_finger_print_page():

        if windowadmin.number_id_fingerprint_save != 2:
            windowFingerPrint.show()
            createFingerprint(windowadmin.enroll_id_fingerprint)
            # creating a blur effect
            windowadmin.ui_admin.blur(3)


        else:
            windowFingerPrint.ui_admin.label_message_number_fingerprint.setText("fingerprint has saved")



def close_page_fingerprint() :
    windowFingerPrint.hide()
    windowadmin.ui_admin.blur(0)
    windowFingerPrint.ui_finger.alarm.setText(" ")
#---------------fingerprint----------------------



def close_save_window():
    windowAlarmEmployee.hide()


def back_dashboard():
    windowadmin.hide()
    window.show()
    windowPassword.hide()
    window.ui.blur(0)





def the_button_was_clicked1():
    if statusLamp[0] == 0:
        publish(client, "", "light1/on")
        window.ui.button_lamp1.setIcon(window.ui.icon_light_on)
        statusLamp[0] = 1

    else:
        publish(client, "", "light1/off")
        window.ui.button_lamp1.setIcon(window.ui.icon_light_off)
        statusLamp[0] = 0


def the_button_was_clicked2():
    if statusLamp[1] == 0:
        publish(client, "", "light2/on")
        window.ui.button_lamp2.setIcon(window.ui.icon_light_on)
        statusLamp[1] = 1

    else:
        publish(client, "", "light2/off")
        window.ui.button_lamp2.setIcon(window.ui.icon_light_off)
        statusLamp[1] = 0


def the_button_was_clicked3():
    if statusLamp[2] == 0:
        publish(client, "", "light3/on")
        window.ui.button_lamp3.setIcon(window.ui.icon_light_on)
        statusLamp[2] = 1

    else:
        publish(client, "", "light3/off")
        window.ui.button_lamp3.setIcon(window.ui.icon_light_off)
        statusLamp[2] = 0


def the_button_was_clicked5():
    if statusLamp[4] == 0:
        publish(client, "", "light3/on")
        window.ui.button_lamp5.setIcon(window.ui.icon_light_on)
        statusLamp[4] = 1

    else:
        publish(client, "", "light3/off")
        window.ui.button_lamp5.setIcon(window.ui.icon_light_off)
        statusLamp[4] = 0


def the_button_was_clicked4():
    if statusLamp[3] == 0:
        publish(client, "", "light3/on")
        window.ui.button_lamp4.setIcon(window.ui.icon_light_on)
        statusLamp[3] = 1

    else:
        publish(client, "", "light3/off")
        window.ui.button_lamp4.setIcon(window.ui.icon_light_off)
        statusLamp[3] = 0


def the_button_was_clicked6():
    if statusLamp[5] == 0:
        publish(client, "", "light6/on")
        window.ui.button_lamp6.setIcon(window.ui.icon_light_on)
        statusLamp[5] = 1

    else:
        publish(client, "", "light6/off")
        window.ui.button_lamp6.setIcon(window.ui.icon_light_off)
        statusLamp[5] = 0


def the_button_was_clicked7():
    if statusLamp[6] == 0:
        publish(client, "", "light7/on")
        window.ui.button_lamp7.setIcon(window.ui.icon_light_on)
        statusLamp[6] = 1

    else:
        publish(client, "", "light7/off")
        window.ui.button_lamp7.setIcon(window.ui.icon_light_off)
        statusLamp[6] = 0


def the_button_was_clicked8():
    if statusLamp[7] == 0:
        publish(client, "", "light8/on")
        window.ui.button_lamp8.setIcon(window.ui.icon_light_on)
        statusLamp[7] = 1

    else:
        publish(client, "", "light8/off")
        window.ui.button_lamp8.setIcon(window.ui.icon_light_off)
        statusLamp[7] = 0

# -----admin page display-------#

def go_to_admin_page():
    window.hide()
    windowadmin.show()
    windowadmin.ui_admin.fram_after_add.show()
    windowadmin.ui_admin.frame_features_one_employee.hide()


def create_new_employee():
    number = windowadmin.get_number_employee()

    global status_crete_employee
    if number <8:
        windowadmin.ui_admin.frame_features_one_employee.show()
        windowadmin.ui_admin.fram_after_add.hide()


        windowadmin.ui_admin.lineEdit_fname.setText(QCoreApplication.translate("MainWindow", "", None))
        windowadmin.ui_admin.lineEdit_Lname.setText(QCoreApplication.translate("MainWindow", "", None))
        windowadmin.ui_admin.label_RFID.setText(QCoreApplication.translate("MainWindow", "", None))
        windowadmin.ui_admin.pushButton_export.hide()
        windowadmin.ui_admin.checkBox_active.hide()
        windowadmin.ui_admin.label_activeOrDi.hide()
        windowadmin.ui_admin.pushButton_save_finger.hide()
        windowadmin.ui_admin.delete_employee.hide()
        windowadmin.ui_admin.label_t_name.setText("Fill")

        id_fingerprint = db.select_number_fingerprint_id()
        windowadmin.ui_admin.label_id_fingerprint.setText(str(id_fingerprint))

        status_crete_employee = 1


    elif number == 8:
        windowadmin.ui_admin.fram_finish_employee()


def save_or_edit_employee():
    lenth = len(windowadmin.get_epmloyees())
    if status_crete_employee == 1:
        firstName = windowadmin.ui_admin.lineEdit_fname.text()
        lastName = windowadmin.ui_admin.lineEdit_Lname.text()

        if lastName == "" or firstName == "" or id_rfid_employee == "":
            windowadmin.ui_admin.label_erro_fill.setText("no fild can not empty")
        else:

            windowadmin.ui_admin.label_erro_fill.setText("")
            number1 = db.select_number_fingerprint_id()
            number2 = number1 + 1
            result = db.maincreatedata(id_rfid_employee, firstName, lastName, str(number1), str(number2), 1)

            if result == True:
                db.update_fingerprint_id(number2 + 1)
                windowAlarmEmployee.show()
                windowAlarmEmployee.ui_alarm_save.labelAlaemEployeeSave.setText("Employee saved")
                windowadmin.ui_admin.lineEdit_fname.setText("")
                windowadmin.ui_admin.lineEdit_Lname.setText("")
                windowadmin.ui_admin.label_RFID.setText("")
                windowadmin.ui_admin.label_id_fingerprint.setText(str(number2 + 1))
                windowadmin.ui_admin.label_t_name.setText("Fill")




                #10/26
                id_person=db.select_return_id(id_rfid_employee)
                p=new_Person(firstName,window.ui.frame_employees)
                temp_array = []
                window.ui.verticalLayout.addWidget(p.config())
                temp_array.append(id_person)
                temp_array.append(p)
                window.array_employee.append(temp_array)


                # update list

                windowadmin.show_button_employee()
                windowadmin.update_list_employee()
                status_crete_employee == 0

            elif result== False:
                windowAlarmEmployee.show()
                windowAlarmEmployee.ui_alarm_save.labelAlaemEployeeSave.setText("UNIQUE idCard failed")


    else:
        # setIDrfid(windowadmin.get_rfid_select_employee())
        # firstName = windowadmin.ui_admin.lineEdit_fname.text()
        # lastName = windowadmin.ui_admin.lineEdit_Lname.text()
        # id_employee=windowadmin.get_id()
        pass

    # db.update_employee_select(firstName,lastName,,id_employee)


##--------------------------------------


# def change_icon_lamp():
#     global icon_light_on, icon_light_off
#     icon_light_on = QIcon()
#     icon_light_off = QIcon()
#     icon_light_on.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btnLamp2.png", QSize(), QIcon.Normal, QIcon.Off)
#     icon_light_off.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btLampOff.png", QSize(), QIcon.Normal, QIcon.Off)



def the_button_door_clicked():
    # icon = QIcon()
    # icon.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/Lockbtn.png", QSize(), QIcon.Normal, QIcon.Off)
    # icon.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btnLamp.png", QSize(), QIcon.Normal, QIcon.On)
    # self.button_door.setIcon(icon)
    publish(client, "", "door/open")


def access_all_button():

    if statusLamp[8] == 0:
        # icon4.addFile(u"D:/V2.0.0/Programme/qt/UI design/picture/btPowerOn.png", QSize(), QIcon.Normal, QIcon.Off)
        window.ui.change_icon_power(0)
        window.ui.label_power.setText(QCoreApplication.translate("MainWindow", u"Turn on", None))
        statusLamp[8] = 1
        publish(client, "", "all/lamp/on")
    else:
        publish(client, "", "all/lamp/off")
        window.ui.change_icon_power(1)
        window.ui.label_power.setText(QCoreApplication.translate("MainWindow", u"Turn off", None))
        statusLamp[8] = 0




function_button()
window.show()
configmqtt()
ui.sys.exit(app.exec_())

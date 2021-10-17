################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from buttontest import Ui_MainWindow


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # self.ui.pushButton.clicked.connect(self.the_button_was_clicked1)



        ## list
        ########################################################################
        # def list_employee(self):
        #     allEmployee = Database.main_select_all_employee()
        #     for i in allEmployee:
        #         self.ui.list_employee.addItem(str(i[0])+"  " +str(i[2]) + " " + str(i[3]))
        #
        #     self.ui.list_employee.itemClicked.connect(self.listwidgetclicked)
        #

        self.show()

    def the_button_was_clicked1(self):
         print("prees")



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

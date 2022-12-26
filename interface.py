import time

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import GetData

print("GO")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Speed = QtWidgets.QLabel(self.centralwidget)
        self.Speed.setGeometry(QtCore.QRect(42, 30, 59, 16))
        self.Speed.setObjectName("Speed")
        self.Alt = QtWidgets.QLabel(self.centralwidget)
        self.Alt.setGeometry(QtCore.QRect(167, 30, 47, 16))
        self.Alt.setObjectName("Alt")
        self.SpeedInfo = QtWidgets.QLabel(self.centralwidget)
        self.SpeedInfo.setGeometry(QtCore.QRect(108, 30, 61, 16))
        speed = GetData.giveSpeed()
        self.SpeedInfo.setText(str(speed))
        self.SpeedInfo.setObjectName("SpeedInfo")
        self.AltInfo = QtWidgets.QLabel(self.centralwidget)
        self.AltInfo.setGeometry(QtCore.QRect(216, 30, 71, 16))
        altitude = GetData.giveAltitude()
        self.AltInfo.setText(str(altitude))
        self.AltInfo.setObjectName("AltInfo")
        self.Kurs = QtWidgets.QLabel(self.centralwidget)
        self.Kurs.setGeometry(QtCore.QRect(285, 30, 31, 16))
        self.Kurs.setObjectName("Kurs")
        self.VSpeedInfo = QtWidgets.QLabel(self.centralwidget)
        self.VSpeedInfo.setGeometry(QtCore.QRect(489, 30, 71, 16))
        vSpeed = GetData.giveVerticalSpeed()
        self.VSpeedInfo.setText(str(vSpeed))
        self.VSpeedInfo.setObjectName("VSpeedInfo")
        self.VSpeed = QtWidgets.QLabel(self.centralwidget)
        self.VSpeed.setGeometry(QtCore.QRect(404, 30, 88, 16))
        self.VSpeed.setObjectName("VSpeed")
        self.KursInfo = QtWidgets.QLabel(self.centralwidget)
        self.KursInfo.setGeometry(QtCore.QRect(320, 30, 81, 16))
        deg = GetData.giveDeg()
        self.KursInfo.setText(str(deg))
        self.KursInfo.setObjectName("KursInfo")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, 120, 231, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(210, 210, 210);")
        self.label.setObjectName("label")

        self.takeoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.button_is_checked = False
        self.takeoffButton.setCheckable(True)
        self.takeoffButton.clicked.connect(self.takeOffToggle)
        self.takeoffButton.setChecked(self.button_is_checked)
        self.takeoffButton.setGeometry(QtCore.QRect(480, 320, 110, 26))
        self.takeoffButton.setStyleSheet("background-color: rgb(210, 210, 210);")
        self.takeoffButton.setObjectName("takeoffButton")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1, 155, 231, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(210, 210, 210);")
        self.label_4.setObjectName("label_4")

        self.textEditSpd = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSpd.setGeometry(QtCore.QRect(232, 120, 120, 31))
        self.textEditSpd.setObjectName("lineSpeed")
        self.textEditAlt = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditAlt.setGeometry(QtCore.QRect(232, 155, 120, 31))
        self.textEditAlt.setObjectName("lineAlt")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlightGear_Interface"))
        self.Speed.setText(_translate("MainWindow", "Скорость:"))
        self.Alt.setText(_translate("MainWindow", "Высота:"))
        self.Kurs.setText(_translate("MainWindow", "Курс:"))
        self.VSpeed.setText(_translate("MainWindow", "Вер. Скорость:"))
        self.label.setText(_translate("MainWindow", "Введите необходимую скорость:"))
        self.takeoffButton.setText(_translate("MainWindow", "TakeOff"))
        self.label_4.setText(_translate("MainWindow", "Введите необходимую высоту:"))

    def takeOffToggle(self):
        self.button_is_checked = self.takeoffButton.isChecked()
        spdtext = self.textEditSpd.toPlainText()
        alttext = self.textEditAlt.toPlainText()
        global takeOff
        takeOff = self.button_is_checked
        print(takeOff, "func")
        if takeOff:
            print(takeOff, "func IN")
            global maxSpeed
            maxSpeed = spdtext
            print(maxSpeed)
            global maxAltitude
            maxAltitude = alttext
            print(maxAltitude)
            Thread(target=getStarted).start()

    @staticmethod
    def getDataSpeed():
        return maxSpeed

    @staticmethod
    def getDataAlt():
        return maxAltitude

def getStarted():
    print("goT")
    time.sleep(1)
    import main

def getMaxSpeed():
    return Ui_MainWindow.getDataSpeed()

def getMaxAlt():
    return Ui_MainWindow.getDataAlt()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
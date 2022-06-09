#!/usr/bin/env python

import time
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.uic import loadUi


bus = SMBus(0)
bme280 = BME280(i2c_dev=bus,i2c_addr=0x76)

class BMEData():
    def __init__(self, temperature=0, pressure=0, humidity=0):
        self.temperature = temperature  
        self.pressure = pressure
        self.humidity = humidity

class ReadThread(QThread):
    data_updated = pyqtSignal(BMEData)
    def run(self):
        while True:
            QThread.sleep(1)
            try:
                temperature = bme280.get_temperature()
                pressure = bme280.get_pressure()
                humidity = bme280.get_humidity()
                self.data_updated.emit(BMEData(temperature, pressure, humidity))
                print('{:05.2f}*C {:05.2f}hPa {:05.2f}%'.format(temperature, pressure, humidity))
            except Exception as e:
                print("Error reading data "+str(e))

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('window.ui', self) # Load the .ui file

        self.thread = ReadThread(self)
        self.thread.data_updated.connect(self.handleSerialUpdate)
        self.thread.start()

        self.show() # Show the GUI

    def handleSerialUpdate(self, value):
        #print(value.temperature, value.pressure, value.humidity)
        try:
            self.lcd_temperature.display(value.temperature)
            self.lcd_humidity.display(value.humidity)
            self.lcd_pressure.display(value.pressure)
        except Exception as e:
            print("Error updating display "+str(e))

        #self.lcd_lineEdit.setText(value)

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class

#File = open("Genetive.qss",'r')
#qss = File.read()
#app.setStyleSheet(qss)
app.exec_() # Start the application

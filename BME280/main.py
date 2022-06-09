import sys, json, serial
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.uic import loadUi


ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

class TestThread(QThread):
    serialUpdate = pyqtSignal(str)
    def run(self):
        while ser.is_open:
            QThread.sleep(1)
            try:
                value = ser.readline().decode('ascii')
                print(value)
                self.serialUpdate.emit(value)
            except UnicodeDecodeError:
                print("UnicodeDecodeError")
            ser.flush()

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('window.ui', self) # Load the .ui file

        self.thread = TestThread(self)
        self.thread.serialUpdate.connect(self.handleSerialUpdate)
        self.thread.start()

        self.show() # Show the GUI

    def handleSerialUpdate(self, value):
        print(value)
        data=json.loads(value)
        try:
            self.lcd_temperature.display(data["Temperature"])
            self.lcd_humidity.display(data["Humidity"])
            self.lcd_pressure.display(data["Pressure"])
        except KeyError:
            print("Invalid JSON")
            print(value)

        #self.lcd_lineEdit.setText(value)

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class

#File = open("Genetive.qss",'r')
#qss = File.read()
#app.setStyleSheet(qss)
app.exec_() # Start the application

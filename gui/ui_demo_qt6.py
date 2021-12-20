from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import *
import sys
from datetime import datetime

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self, data_key):
        self.label.setText("{}: {} - clicked\n{}".format( datetime.now().strftime("%H:%M:%S"), data_key,self.label.text()))

    def initBtn(self, btn, data_key, x, y, w=240, h=30):
        btn.setText(data_key)
        btn.clicked.connect(lambda: self.button_clicked(data_key))
        btn.move(x,y)        
        btn.resize(w, h)

    def initUI(self):
        self.setGeometry(10, 60, 700, 400)
        self.setWindowTitle("Demo")

        self.label = QtWidgets.QLabel(self)
        self.label.setText(datetime.now().strftime("%H:%M:%S") + ": ...")
        self.label.move(260,3) 
        self.label.setWordWrap(True)   
        self.label.resize(380, 380)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(4, 4, 238, 28)
        self.comboBox.addItems(['Option A', 'Option B']) 
        self.comboBox.activated.connect(lambda: self.button_clicked(self.comboBox.currentText()))
        
        self.initBtn(QtWidgets.QPushButton(self), 'Button A', 3, 33)
        self.initBtn(QtWidgets.QPushButton(self), 'Button B', 3, 63)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    window()
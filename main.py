from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("helper.ui", self)

        # Configure quit quitButton
        self.quitbutton = self.findChild(QPushButton, "quitButton")
        self.quitbutton.clicked.connect(self.QuitClicked)

        # Get status label
        self.statuslabel = self.findChild(QLabel, "statusLabel")

        self.show()

    def QuitClicked(self):
        exit()

app = QApplication(sys.argv)
window = UI()
app.exec_()

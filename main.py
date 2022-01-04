#UI
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLabel, QDialog
from PyQt5 import uic
from PyQt5.uic import loadUi

#Functionality
import os
import sys
import subprocess

class SystemInformationDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi("dialogs/systeminfo.ui", self)

        self.quitButton = self.findChild(QPushButton, "quitButton")
        self.quitButton.clicked.connect(self.QuitButton)

    def QuitButton(self):
        quit()





class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("helper.ui", self)

        # Configure quit quitButton
        self.quitButton = self.findChild(QPushButton, "quitButton")
        self.quitButton.clicked.connect(self.QuitClicked)

        # Get status label
        self.statusLabel = self.findChild(QLabel, "statusLabel")

        #System tab

        # Clear cache Button
        self.clearCacheButton = self.findChild(QPushButton, "clearCacheButton")
        self.clearCacheButton.clicked.connect(self.ClearCache)

        # System Information Button
        self.systemInfoButton = self.findChild(QPushButton, "systemInfoButton")
        self.systemInfoButton.clicked.connect(self.SystemInformation)

        self.show()

    def QuitClicked(self):
        exit()

    def ClearCache(self):
        self.statusLabel.setText("Awaiting authentication...") # This does not seem to work
        status = os.system("sudo sysctl vm.drop_caches=3")
        if status == 0:
            self.statusLabel.setText("Cache cleared!")
        else:
            self.statusLabel.setText("Error:", str(status))

    def SystemInformation(self):
        dialog = SystemInformationDialog()
        dialog.exec()


app = QApplication(sys.argv)
window = UI()
app.exec_()

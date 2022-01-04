#UI
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLabel, QDialog
from PyQt5 import uic
from PyQt5.uic import loadUi

#Functionality
import os
import sys
import subprocess
import platform
import distro

class SystemInformationDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi("dialogs/systeminfo.ui", self)



        self.architectureLabel = self.findChild(QLabel, "architectureLabel")
        self.architectureLabel.setText("Architecture: "+platform.architecture()[0])

        self.hostnameLabel = self.findChild(QLabel, "hostnameLabel")
        self.hostnameLabel.setText("Hostname: "+platform.node())

        self.distroLabel = self.findChild(QLabel, "distroLabel")
        self.distroLabel.setText("Distro: "+ distro.id())

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

        # Update button
        self.updateButton = self.findChild(QPushButton, "updateButton")
        self.updateButton.clicked.connect(self.UpdateSystem)

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
        self.statusLabel.setText("Showing system information")
        dialog = SystemInformationDialog()
        dialog.exec()

    def UpdateSystem(self):
        self.statusLabel.setText("Updating...")
        distroid = distro.id()
        with open("data/package-managers.txt", "r") as pml:
            for line in pml:
                if distroid in line:
                    pm = line.split(" ")[0]
        if pm == "apt":
            self.statusLabel.setText("Updating system (apt)")
            status = os.system("sudo apt-get upgrade && sudo apt-get update -y")
            if status == 0:
                self.statusLabel.setText("Update finished!")
            else:
                self.statusLabel.setText("Update error:", status)

        if pm == "pacman":
            self.statusLabel.setText("Updating system (pacman)")
            status = os.system("sudo pacman -Syu")
            if status == 0:
                self.statusLabel.setText("Update finished!")
            else:
                self.statusLabel.setText("Update error:", status)
        else:
            self.statusLabel.setText("Unknown distro. Report on GitHub.")



app = QApplication(sys.argv)
window = UI()
app.exec_()

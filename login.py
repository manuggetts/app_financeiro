from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal
from animated_button import AnimatedButton
from PyQt5.QtGui import QIcon
from sys import exit
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class LoginWindow(QtWidgets.QMainWindow):
    login_success = pyqtSignal(str)

    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('design1.ui', self)

        self.setWindowIcon(QIcon(':/img/favico.png'))

        self.Username = self.findChild(QLineEdit, 'Username')
        self.Password = self.findChild(QLineEdit, 'Password')
        self.Login = self.findChild(AnimatedButton, 'Login')

        self.Login.setStyleSheet("""
                AnimatedButton {
                    background: none;
                    border-radius: 15px;
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                                        stop:0 #ff8c00, stop:0.5 #ffa500, stop:1 #ffbf00);
                    color: #fff;
                    border: none;
                    font: bold;
                    }

                    AnimatedButton:hover {
                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                                        stop:0 #ffbf00, stop:0.5 #ffa500, stop:1 #ff8c00);
                    }
                """)

        self.Password.setEchoMode(QLineEdit.Password)
        self.Login.clicked.connect(self.login)

    def login(self):
        username = self.Username.text()
        self.login_success.emit(username)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.Login.click()
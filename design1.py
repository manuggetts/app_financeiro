from PyQt5 import QtCore, QtWidgets
from animated_button import AnimatedButton
import resources

class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(781, 622)
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, -10, 801, 591))
        self.widget.setStyleSheet("background-image: url(:/img/pag1.png);")
        self.widget.setObjectName("widget")
        self.Username = QtWidgets.QLineEdit(self.widget)
        self.Username.setGeometry(QtCore.QRect(310, 320, 191, 31))
        self.Username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Username.setStyleSheet("font: bold; \n"
"color: #000000;\n"
"border-radius: 15;\n"
"background: #fff;")
        self.Username.setText("")
        self.Username.setCursorPosition(0)
        self.Username.setAlignment(QtCore.Qt.AlignCenter)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(310, 360, 191, 31))
        self.Password.setStyleSheet("font: bold; \n"
"color: #000000;\n"
"border-radius: 15;\n"
"background: #fff;")
        self.Password.setText("")
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")
        self.Login = AnimatedButton(self.widget)
        self.Login.setGeometry(QtCore.QRect(360, 400, 91, 31))
        self.Login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Login.setStyleSheet("AnimatedButton:focus {outline: none;}")
        self.Login.setObjectName("Login")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(270, 320, 31, 31))
        self.widget_2.setStyleSheet("image: url(:/img/username.png);\n"
"border-radius: 15;\n"
"background: transparent;")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(270, 360, 31, 31))
        self.widget_3.setStyleSheet("image: url(:/img/senha.png);\n"
"border-radius: 15;\n"
"background: transparent;")
        self.widget_3.setObjectName("widget_3")
        self.Username.raise_()
        self.Password.raise_()
        self.widget_3.raise_()
        self.Login.raise_()
        self.widget_2.raise_()
        Inicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName("menubar")
        Inicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Inicio)
        self.statusbar.setObjectName("statusbar")
        Inicio.setStatusBar(self.statusbar)

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Controle Financeiro"))
        self.Username.setToolTip(_translate("Inicio", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\"><br/></span></p></body></html>"))
        self.Username.setWhatsThis(_translate("Inicio", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Username.setPlaceholderText(_translate("Inicio", "Username"))
        self.Password.setPlaceholderText(_translate("Inicio", "Password"))
        self.Login.setText(_translate("Inicio", "Login"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio = QtWidgets.QMainWindow()
    ui = Ui_Inicio()
    ui.setupUi(Inicio)
    Inicio.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from animated_button import AnimatedButton
import resources

class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(783, 628)
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 801, 601))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(55, 420, 691, 131))
        self.tableWidget.setStyleSheet("""
        QTableWidget {
                background: none;
                background-color: #fff;
                border-radius: 15;
                selection-background-color: transparent;
        }""")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btt_entrada = QtWidgets.QLabel(self.widget)
        self.btt_entrada.setGeometry(QtCore.QRect(50, 70, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btt_entrada.setFont(font)
        self.btt_entrada.setStyleSheet("background: none;\n"
"color: #fff;")
        self.btt_entrada.setText("")
        self.btt_entrada.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.btt_entrada.setObjectName("btt_entrada")
        self.btt_saida = QtWidgets.QLabel(self.widget)
        self.btt_saida.setGeometry(QtCore.QRect(310, 70, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btt_saida.setFont(font)
        self.btt_saida.setStyleSheet("background: none;\n"
"color: #fff;")
        self.btt_saida.setText("")
        self.btt_saida.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.btt_saida.setObjectName("btt_saida")
        self.btt_total = QtWidgets.QLabel(self.widget)
        self.btt_total.setGeometry(QtCore.QRect(570, 70, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btt_total.setFont(font)
        self.btt_total.setStyleSheet("background: none;\n"
"color: #fff;")
        self.btt_total.setText("")
        self.btt_total.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.btt_total.setObjectName("btt_total")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 250, 181, 41))
        self.lineEdit.setStyleSheet("background: #fff;\n"
"border-radius: 15;\n"
"background-color: #B9B7B7;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 250, 181, 41))
        self.lineEdit_2.setStyleSheet("background: #fff;\n"
"border-radius: 15;\n"
"background-color: #B9B7B7;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btt_entrada_2 = QtWidgets.QLabel(self.widget)
        self.btt_entrada_2.setGeometry(QtCore.QRect(80, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btt_entrada_2.setFont(font)
        self.btt_entrada_2.setStyleSheet("background: none;\n"
"color: #252931;\n"
"font: bold;")
        self.btt_entrada_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.btt_entrada_2.setObjectName("btt_entrada_2")
        self.btt_entrada_3 = QtWidgets.QLabel(self.widget)
        self.btt_entrada_3.setGeometry(QtCore.QRect(280, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btt_entrada_3.setFont(font)
        self.btt_entrada_3.setStyleSheet("background: none;\n"
"color: #252931;\n"
"font: bold;")
        self.btt_entrada_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.btt_entrada_3.setObjectName("btt_entrada_3")
        self.Entrada = QtWidgets.QRadioButton(self.widget)
        self.Entrada.setGeometry(QtCore.QRect(480, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Entrada.setFont(font)
        self.Entrada.setStyleSheet("""
        QRadioButton {
                background: none;
                border-radius: 15;
        }

        QRadioButton:focus {
                outline: none;
        }
        """)
        self.Entrada.setObjectName("Entrada")
        self.Saida = QtWidgets.QRadioButton(self.widget)
        self.Saida.setGeometry(QtCore.QRect(480, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Saida.setFont(font)
        self.Saida.setStyleSheet("""
        QRadioButton {
                background: none;
                border-radius: 15;
        }

        QRadioButton:focus {
                outline: none;
        }
        """)
        self.Saida.setObjectName("Saida")
        self.pushButton = AnimatedButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(590, 230, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet()
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 811, 601))
        self.frame.setStyleSheet("background-image: url(:/img/pag2.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: none;\n"
"color: #fff;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: none;\n"
"color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(570, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: none;\n"
"color: #fff;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame.raise_()
        self.tableWidget.raise_()
        self.btt_entrada.raise_()
        self.btt_saida.raise_()
        self.btt_total.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.btt_entrada_2.raise_()
        self.btt_entrada_3.raise_()
        self.Entrada.raise_()
        self.Saida.raise_()
        self.pushButton.raise_()
        Inicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
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
        self.btt_entrada_2.setText(_translate("Inicio", "Descrição"))
        self.btt_entrada_3.setText(_translate("Inicio", "Valor"))
        self.Entrada.setText(_translate("Inicio", "Entrada"))
        self.Saida.setText(_translate("Inicio", "Saída"))
        self.pushButton.setText(_translate("Inicio", "ADICIONAR"))
        self.label_2.setText(_translate("Inicio", "Saídas"))
        self.label.setText(_translate("Inicio", "Entradas"))
        self.label_3.setText(_translate("Inicio", "Total"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio = QtWidgets.QMainWindow()
    ui = Ui_Inicio()
    ui.setupUi(Inicio)
    Inicio.show()
    sys.exit(app.exec_())

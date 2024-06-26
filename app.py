from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QLabel, QTableWidget
from PyQt5.QtGui import QIcon
from animated_button import AnimatedButton
from sys import argv, exit
from login import LoginWindow
import resources

class ControleFinanceiro(QtWidgets.QMainWindow):
    def __init__(self):
        super(ControleFinanceiro, self).__init__()
        uic.loadUi('design2.ui', self)

        self.setWindowIcon(QIcon(':/img/favico.png'))

        self.valor_entrou = 0
        self.valor_saiu = 0
        self.valor_total = 0

        self.lineEdit = self.findChild(QLineEdit, 'lineEdit')
        self.lineEdit_2 = self.findChild(QLineEdit, 'lineEdit_2')
        self.Entrada = self.findChild(QRadioButton, 'Entrada')
        self.Saida = self.findChild(QRadioButton, 'Saida')
        self.pushButton = self.findChild(AnimatedButton, 'pushButton')
        self.btt_entrada = self.findChild(QLabel, 'btt_entrada')
        self.btt_saida = self.findChild(QLabel, 'btt_saida')
        self.btt_total = self.findChild(QLabel, 'btt_total')
        self.tableWidget = self.findChild(QTableWidget, 'tableWidget')

        font = QtGui.QFont()
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)

        nomes_colunas = ['Descrição', 'Valor', 'Tipo', 'Data', 'Hora']
        self.tableWidget.setColumnCount(len(nomes_colunas))
        self.tableWidget.setHorizontalHeaderLabels(nomes_colunas)

        self.pushButton.clicked.connect(self.adicionar_item)

    def adicionar_item(self):
        descricao = self.lineEdit.text()
        valor_texto = self.lineEdit_2.text().replace(',', '.')

        try:
            valor = float(valor_texto)
            if valor <= 0:
                print("O valor deve ser positivo.")
                return
        except ValueError:
            print(f"Não foi possível converter '{valor_texto}' em um número.")
            return

        entrada = self.Entrada.isChecked()
        saida = self.Saida.isChecked()

        if entrada:
            self.valor_entrou += valor
            self.valor_total += valor
            tipo = '+'
        elif saida:
            self.valor_saiu += valor
            self.valor_total -= valor
            tipo = '-'

        self.btt_entrada.setText('R$ {:,.2f}'.format(self.valor_entrou))
        self.btt_saida.setText('R$ {:,.2f}'.format(self.valor_saiu))
        self.btt_total.setText('R$ {:,.2f}'.format(self.valor_total))

        current_datetime = QtCore.QDateTime.currentDateTime()
        data_str = current_datetime.toString("dd/MM/yy")
        hora_str = current_datetime.toString("hh:mm:ss")

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        
        items_list = [
            QtWidgets.QTableWidgetItem(descricao),
            QtWidgets.QTableWidgetItem('R$ {:,.2f}'.format(valor)),
            QtWidgets.QTableWidgetItem(tipo),
            QtWidgets.QTableWidgetItem(data_str),
            QtWidgets.QTableWidgetItem(hora_str)
        ]
        
        for col, item in enumerate(items_list):
            item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(row_position, col, item)

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        
app = QtWidgets.QApplication(argv)
login_window = LoginWindow()

def open_main_window():
    print("Abrindo a janela principal...")
    try:
      login_window.main_window = ControleFinanceiro()
      login_window.main_window.show()
      print("Janela principal aberta com sucesso!")
      login_window.close()
    except Exception as e:
      print("Erro ao abrir a janela principal:", e)

login_window.login_success.connect(open_main_window)
login_window.show()

exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.esquerda = 100
        self.topo = 100
        self.largura = 600
        self.altura = 800
        self.titulo = "Compras do mes"

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def addProdduto():
        self.produto = (self.produto, '\n' )

aplicacao = QApplication(sys.argv) 
j = Janela() 
sys.exit(aplicacao.exec_())

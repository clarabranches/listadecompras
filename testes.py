from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table_produtos = QTableWidget(10, 3, self)  # Tabela com 10 linhas e 3 colunas
        self.table_produtos.setGeometry(50, 50, 400, 300)  # Posição e tamanho da tabela
        self.setWindowTitle("Supermercado")

        self.button_add = QPushButton('Adicionar Linha', self)
        self.button_add.setGeometry(50, 370, 150, 30)
        self.button_add.clicked.connect(self.add_row)

        # Layout para facilitar a organização dos widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table_produtos)
        layout.addWidget(self.button_add)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_row(self):
        row_position = self.table_produtos.rowCount()
        self.table_produtos.insertRow(row_position)

        self.table_produtos.setItem(row_position, 0, QTableWidgetItem("Novo Produto"))
        self.table_produtos.setItem(row_position, 1, QTableWidgetItem("0.00"))
        self.table_produtos.setItem(row_position, 2, QTableWidgetItem("1"))

        # Cria o botão e adiciona à tabela
        btn = QPushButton('Ação')
        btn.clicked.connect(lambda: self.button_clicked(row_position))
        self.table_produtos.setCellWidget(row_position, 2, btn)

    def button_clicked(self, row):
        print(f"Botão da linha {row} clicado")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    sys.exit(app.exec_())
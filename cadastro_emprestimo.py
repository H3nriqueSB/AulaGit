import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from controllers.biblioteca import biblioteca

ui_file = 'views/CadastroEmprestimo.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.butcad.clicked.connect(self.click_cad)

        self.biblioteca = biblioteca()

    def click_cad(self):
        textuser = self.lineuser.text()
        textisbn = self.lineisbn.text()
        textlivro = self.linelivro.text()

        self.biblioteca.cadastrar_emprestimo(usuario=textuser, isbn=textisbn, livro=textlivro)

        print("Nome do Cliente:", textuser)
        print("ISBN:", textisbn)
        print("Livro:", textlivro)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

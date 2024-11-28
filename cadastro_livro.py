import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from controllers.biblioteca import biblioteca

ui_file = 'views/CadastroLivro.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.butcad.clicked.connect(self.click_cad)

        self.biblioteca = biblioteca()

    def click_cad(self):
        textitulo = self.linetitulo.text()
        textautor = self.lineautor.text()
        textisbn = self.lineisbn.text()
        textgenero = self.linegenero.text()

        self.biblioteca.cadastrar_livro(titulo=textitulo, autor=textautor, isbn=textisbn, genero=textgenero)

        print("Título:", textitulo)
        print("Autor:", textautor)
        print("ISBN:", textisbn)
        print("Gênero:", textgenero)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

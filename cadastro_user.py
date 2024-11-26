import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from controllers.biblioteca import biblioteca

ui_file = 'views/CadastroUser.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.cadastro.clicked.connect(self.click_cad)

        self.biblioteca = biblioteca()

    def click_cad(self):
        nametext = self.linename.text()
        cpftext = self.linecpf.text()
        emailtext = self.linemail.text()
        senhatext = self.linesenha.text()

        self.biblioteca.cadastrar_usuario(nome=nametext, email=emailtext, senha=senhatext, cpf=cpftext)

        print("Nome:", nametext)
        print("CPF:", cpftext)
        print("Email:", emailtext)
        print("Senha", senhatext)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

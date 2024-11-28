import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from controllers.biblioteca import biblioteca

ui_file = 'views/Login.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.butcad.clicked.connect(self.click_login)

        self.biblioteca = biblioteca()

    def click_login(self):
        usuario = self.lineusuario.text()  
        senha = self.linesenha.text()

        if self.validar_login(usuario, senha):
            print(f"Login bem-sucedido para o usuário: {usuario}")

        else:
            print("Erro: Usuário ou senha incorretos.")

    def validar_login(self, usuario, senha):
        usuario_valido = "admin"
        senha_valida = "12345"

        return usuario == usuario_valido and senha == senha_valida

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

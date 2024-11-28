import sys
import sqlite3
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

        # Instanciando a biblioteca
        self.biblioteca = biblioteca()

    def click_cad(self):
        # Coleta os dados do formulário
        nametext = self.linename.text()
        cpftext = self.linecpf.text()
        emailtext = self.linemail.text()
        senhatext = self.linesenha.text()

        # Chama o método para cadastrar o usuário no banco de dados
        self.biblioteca.cadastrar_usuario(nome=nametext, email=emailtext, senha=senhatext, cpf=cpftext)

        # Exibe as informações para o console (para depuração)
        print("Nome:", nametext)
        print("CPF:", cpftext)
        print("Email:", emailtext)
        print("Senha:", senhatext)


class biblioteca:
    def __init__(self):
        # Conexão com o banco de dados SQLite
        self.conn = sqlite3.connect('usuarios.db')
        self.c = self.conn.cursor()

    def cadastrar_usuario(self, nome, email, senha, cpf):
        try:
            # Inserir os dados do usuário na tabela
            self.c.execute('''
                INSERT INTO usuarios (nome, cpf, email, senha)
                VALUES (?, ?, ?, ?)
            ''', (nome, cpf, email, senha))

            # Salva as alterações no banco
            self.conn.commit()
            print("Usuário cadastrado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
        finally:
            # Sempre feche a conexão após a operação
            self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

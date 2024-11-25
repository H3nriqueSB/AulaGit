import sqlite3
from datetime import datetime

class Livro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.disponivel = True

    def atualizar(self, titulo=None, autor=None, genero=None):
        if titulo:
            self.titulo = titulo
        if autor:
            self.autor = autor
        if genero:
            self.genero = genero

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

class Usuario:
    def __init__(self, nome_completo, email, senha, cpf):
        self.nome_completo = nome_completo
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.admin = False
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        if len(self.emprestimos) < 3:
            self.emprestimos.append(emprestimo)
            return True
        return False

    def devolver_emprestimo(self, emprestimo):
        if emprestimo in self.emprestimos:
            self.emprestimos.remove(emprestimo)
            return True
        return False

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def devolver(self):
        self.data_devolucao = datetime.now()
        self.livro.devolver()
        self.usuario.devolver_emprestimo(self)

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, titulo, autor, isbn, genero):
        if not any(livro.isbn == isbn for livro in self.livros):
            novo_livro = Livro(titulo, autor, isbn, genero)
            self.livros.append(novo_livro)
            return True
        return False

    def consultar_livro(self, **kwargs):
        resultados = [livro for livro in self.livros if all(getattr(livro, k) == v for k, v in kwargs.items())]
        return resultados

    def cadastrar_usuario(self, nome_completo, email, senha, cpf):
        if not any(usuario.email == email for usuario in self.usuarios):
            novo_usuario = Usuario(nome_completo, email, senha, cpf)
            self.usuarios.append(novo_usuario)
            return True
        return False

    def realizar_emprestimo(self, email_usuario, isbn_livro):
        usuario = next((u for u in self.usuarios if u.email == email_usuario), None)
        livro = next((l for l in self.livros if l.isbn == isbn_livro), None)
        if usuario and livro and livro.emprestar():
            emprestimo = Emprestimo(usuario, livro)
            usuario.adicionar_emprestimo(emprestimo)
            return True
        return False

    def devolver_emprestimo(self, email_usuario, isbn_livro):
        usuario = next((u for u in self.usuarios if u.email == email_usuario), None)
        emprestimo = next((e for e in usuario.emprestimos if e.livro.isbn == isbn_livro), None)
        if emprestimo:
            emprestimo.devolver()
            return True
        return False

def conectar_banco():
    conn = sqlite3.connect('biblioteca.db')
    return conn

def criar_tabelas():
    conn = conectar_banco()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS livros
                 (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, isbn TEXT UNIQUE, genero TEXT, disponivel INTEGER)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY, nome_completo TEXT, email TEXT UNIQUE, senha TEXT, cpf TEXT UNIQUE, admin INTEGER)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS emprestimos
                 (id INTEGER PRIMARY KEY, id_usuario INTEGER, id_livro INTEGER, data_emprestimo TEXT, data_devolucao TEXT,
                  FOREIGN KEY(id_usuario) REFERENCES usuarios(id),
                  FOREIGN KEY(id_livro) REFERENCES livros(id))''')
    
    conn.commit()
    conn.close()

criar_tabelas()

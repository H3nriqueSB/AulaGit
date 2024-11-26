import sqlite3
from datetime import datetime

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

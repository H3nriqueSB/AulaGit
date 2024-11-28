from datetime import datetime

class Emprestimo:
    def __init__(self, usuario, livro, isbn):
        self.usuario = usuario
        self.livro = livro
        self.isbn = isbn
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
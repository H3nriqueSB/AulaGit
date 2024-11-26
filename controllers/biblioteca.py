from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from datetime import datetime
from models.usuario import Usuario

class biblioteca ():
    def __init__(self) -> None:
        self.livros = []
        self.usuarios = []

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
    

    def devolver(self):
        self.data_devolucao = datetime.now()
        self.livro.devolver()
        self.usuario.devolver_emprestimo(self)


    def cadastrar_livro(self, titulo, autor, isbn, genero):
        if not any(livro.isbn == isbn for livro in self.livros):
            novo_livro = Livro(titulo, autor, isbn, genero)
            self.livros.append(novo_livro)
            return True
        return False

    def consultar_livro(self, **kwargs):
        resultados = [livro for livro in self.livros if all(getattr(livro, k) == v for k, v in kwargs.items())]
        return resultados
        
    
    def cadastrar_usuario(self, nome, email, senha, cpf):
        if not any(usuario.email == email for usuario in self.usuarios):
            novo_usuario = Usuario(nome, email, senha, cpf)
            self.usuarios.append(novo_usuario)  # Remova o ponto extra aqui

            return True
        return False

    # @staticmethod
    # def cadastrar_usuario(nome, email, senha, cpf):
    #     if not any(usuario.email == email for usuario in biblioteca.usuarios):
    #         novo_usuario = Usuario(nome, email, senha, cpf)
    #         biblioteca.usuarios.append(novo_usuario)
    #         return True
    #     return False

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
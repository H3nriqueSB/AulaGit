class usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_empre(self, livro):
        if len(self.lista_livros)
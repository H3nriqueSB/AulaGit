class Usuario:
    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.admin = False
        self.emprestimos = []
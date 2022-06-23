class Funcionario:

    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.bonificacao = 100

    def __str__(self):
        return f"Nome: {self.nome}\ncpf: {self.cpf}\nsalario: {self.salario}\nbonificacao: {self.bonificacao}\n"

    def get_bonificacao(self):
        return self.bonificacao


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):

        return super().get_bonificacao()*1.5

    def __str__(self):
        return f"Nome: {self.nome}\ncpf: {self.cpf}\nsalario: {self.salario}\nbonificacao: {self.get_bonificacao()}\n"


class Diretoria(Funcionario):
    def __init__(self, nome, cpf, salario, carro):
        super().__init__(nome, cpf, salario)
        self.carro = carro

    def get_bonificacao(self):
        return super().get_bonificacao()*5

    def __str__(self):
        return f"Nome: {self.nome}\ncpf: {self.cpf}\nsalario: {self.salario}\nbonificacao: {self.get_bonificacao()}\ncarro: {self.carro}\n"


funcionario = Funcionario("Igor Funcionario", "012930129", 1500)

print(funcionario)

gerente = Gerente("Fernando Gerente", "123123123", 1800)
print(gerente)

diretoria = Diretoria("Joao Diretor", "123123", 5000, "Fusca")
print(diretoria)

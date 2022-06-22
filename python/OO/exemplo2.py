
class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nProfissao: {self.profissao}\n\n"


listagem1 = [
    {'nome': 'joao', 'idade': 20, 'profissao': "estudante"},
    {'nome': 'Igor', 'idade': 22, 'profissao': "Programador"}
]

listagemPessoas = []

print(listagem1)

for item in listagem1:
    pessoa = Pessoa(item['nome'], item['idade'], item['profissao'])
    listagemPessoas.append(pessoa)

for pessoa in listagemPessoas:
    print(pessoa)
    pessoa.save()

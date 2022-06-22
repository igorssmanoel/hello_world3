class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"


pessoas = [Pessoa("igor", 28), Pessoa("Ricardo", 40)]

for pessoa in pessoas:
  print(pessoa.nome)

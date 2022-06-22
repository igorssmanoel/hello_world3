





# Tem motor e se move
class Automovel:
    """Documentação: Classe responsavel por armazenar dados de um automovel"""
      
    def __init__(self, modelo, marca, cor, tamanho_roda, combustivel='gasolina', ano=2000):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.tamanho_roda = tamanho_roda
        self.combustivel = combustivel
        self.ano = ano

    def __str__(self):
        return f"{self.modelo}, {self.marca}, {self.cor}, {self.tamanho_roda}, {self.combustivel}, {self.ano}"

    def __eq__(self, outroAutomovel):
      if (isinstance(outroAutomovel, self.__class__)):
        return self.modelo == outroAutomovel.modelo and self.marca == outroAutomovel.marca
      else:
        return False

    def move(self):
        print(f"{self.modelo} se moveu")

    def freia(self):
        print(f"{self.modelo} freiou")

    def virar(self, direcao):
        print(f"{self.modelo} virou para {direcao}")


automovel1 = Automovel("Gol", "VW", "Preto", 17)
print(automovel1)
automovel1.move()
automovel1.virar('direita')
automovel1.freia()

print(automovel1.__doc__)

automovel2 = Automovel("Fusca", "VW", "Vermelho", 17, 'alcool', 1987)
print(automovel2)
automovel2.move()


if (automovel1 == automovel2):
  print("são iguais")
else:
  print("Automovel 1 nao eh igual ao automovel 2")

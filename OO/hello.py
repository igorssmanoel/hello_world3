# Uma classe é composta de métodos e atributos

class Calculadora:
  def __init__(self, descricao):
    self.descricao = descricao

  def soma(self,a,b):
    return a+b

  def subtracao(self,a,b):
    return a-b

  def multiplicacao(self,a,b):
    return a*b

  def divisao(self,a,b):
    return a/b
 
meuObjeto = Calculadora("Essa é minha primeira calculadora") #Inicializando objeto

print(meuObjeto.descricao) ## Acessando atributo do objeto

print(meuObjeto.soma(3, 5))

meuSegundoObjeto = Calculadora("Essa é minha outra calculadora")

print(meuSegundoObjeto.descricao)
print(meuObjeto.descricao)




class Pessoa:
  #atributos
  # Nome
  # Cpf
  # Nascimento
  # Altura
  # Peso

  #metodo
  # Imprimir o resumo

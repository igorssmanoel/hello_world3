def soma(a: int,b: int):
  return a+b

def imprimeFormatado(numero):
  print("SOMA = %d" % (numero))

def resolve_exercicio():
  a = int(input())
  b = int(input())

  imprimeFormatado(soma(a,b))

resolve_exercicio()

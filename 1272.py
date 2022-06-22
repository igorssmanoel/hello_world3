#Mensagem oculta

qtdCasos = int(input())

for i in range(qtdCasos):
  linha = input()
  itensSplitados = linha.split(" ")

  result = ""
  for item in itensSplitados:
    if (len(item)>0):
      result += item[0]
  print(result)

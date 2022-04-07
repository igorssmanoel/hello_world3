qtd_casos = int(input())

dicionario = {}

for i in range(qtd_casos):
  caso = int(input())
  if caso not in dicionario.keys():
    dicionario[caso] = 1
  else:
    dicionario[caso] += 1
  
keys_ordenadas = sorted(dicionario)
for key in keys_ordenadas:
  print(f"{key} aparece {dicionario[key]} vez(es)")



a,b = list(map(int, input().split())) 

while not (a == 0 and b == 0):
  soma = a + b
  somaStr = str(soma)

  resultado = somaStr.replace("0", "")

  print(resultado)
  a,b = list(map(int, input().split())) 
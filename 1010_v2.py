total = 0

for i in range(0,2):
  linha = input().split()
  qtd = int(linha[1])
  valor = float(linha[2])
  total += qtd * valor

print(f"VALOR A PAGAR: R$ {total:.2f}")



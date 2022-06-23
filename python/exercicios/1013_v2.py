linha = input().split()

a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

# comparar 2 a 2 e ver qual é maior
maior = (a+b + abs(a-b))/2

maior = (maior + c + abs(maior-c))/2

print(f"{int(maior)} eh o maior")



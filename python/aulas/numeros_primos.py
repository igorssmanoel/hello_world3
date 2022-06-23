# Numero primo é todo numero que é divisivel somente por 1 e por ele mesmo

numero = 53

ehPrimo = True
for i in range(2, int(numero**(1/2))):  # for i in range(2,numero):
    if (numero % i == 0):
        ehPrimo = False
        break

print(f"Foi feito {i} verificações")

if (ehPrimo):
    print(f"{numero} É um numero primo")
else:
    print(f"{numero} Não é um número primo")

linha1 = input().split()
linha2 = input().split()

qtdA = int(linha1[1])
valorA = float(linha1[2])

qtdB = int(linha2[1])
valorB = float(linha2[2])

totalA = qtdA * valorA
totalB = qtdB * valorB

total = totalA + totalB

print(f"VALOR A PAGAR: R$ {total:.2f}")



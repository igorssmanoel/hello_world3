a, b, c, d = input().split(" ")

pesoA = 2
pesoB = 3
pesoC = 4
pesoD = 1

a = float(a)*pesoA
b = float(b)*pesoB
c = float(c)*pesoC
d = float(d)*pesoD


media = (a+b+c+d)/(pesoA+pesoB+pesoC+pesoD)

print(f"Media: {media:.1f}")

if (media >= 7):
    print("Aluno aprovado.")
elif (media < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaExame = float(input())
    print(f"Nota do exame: {notaExame:.1f}")
    novaMedia = (notaExame + media) / 2
    if (novaMedia >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {novaMedia:.1f}")

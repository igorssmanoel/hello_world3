primeira_nota = int(input("Digite o primeiro numero: "))
segunda_nota = int(input("Digite o segundo numero: "))

media = (primeira_nota + segunda_nota) / 2

print("A media das notas é " + str(media))

if (media >= 6):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

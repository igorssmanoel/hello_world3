nome = input("Digite seu nome: ")

primeira_nota = int(input("Digite a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

print("A media das notas do "+ nome  +" é " + str(media))


if (( media >= 6 ) or (nome == "Igor Manoel")):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

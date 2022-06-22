

def popula_pessoas() -> list:
    pessoas = []
    nome = input("Digite o nome da pessoa: ")

    while (nome != "FIM"):
        idade = input("Digite a idade da pessoa: ")
        pessoa = {"nome": nome, "idade": idade}

        pessoas.append(pessoa)
        nome = input("Digite o nome da pessoa: ")
    return pessoas


def imprime_pessoas(pessoas) -> None:
    for pessoa in pessoas:
        print(f"O {pessoa['nome']} tem {pessoa['idade']} anos.")


pessoas_lidas = popula_pessoas()
imprime_pessoas(pessoas_lidas)

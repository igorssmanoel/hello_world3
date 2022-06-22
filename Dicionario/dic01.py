dic = {
    "banana": {
        "nanica": "15,00",
        "prata": "3,00"
    },
    "maça": "12,00"
}


separador = ", "

frutas_disponiveis = separador.join(list(dic.keys()))

print(f"As seguintes frutas estão disponiveis: {frutas_disponiveis}")

fruta = input("Digite qual fruta deseja saber o preço: ")

if ( isinstance(dic[fruta], dict) ):
  frutas_texto = separador.join(list(dic[fruta].keys()))

  print(f"Existem as seguintes variações: {frutas_texto}")
  variacao = input(f"Digite o nome da variação da fruta {fruta}: ")
  frase = f"O preco da {fruta} {variacao} é R$ {dic[fruta][variacao]} o Kg."
  
elif ( isinstance(dic[fruta], str) ):
  frase = f"O preco da {fruta} é R$ {dic[fruta]} o Kg."


print(frase)




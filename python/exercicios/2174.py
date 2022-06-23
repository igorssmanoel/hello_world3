qtd_linhas = int(input())

pokemons_capturados = []

for i in range(qtd_linhas):
  pokemon = input()

  if (pokemon not in pokemons_capturados):
    pokemons_capturados.append(pokemon)

qtd_pokemons_capturados =  len(pokemons_capturados)

quantos_faltam = 151 - qtd_pokemons_capturados

print(f"Falta(m) {quantos_faltam} pomekon(s).")

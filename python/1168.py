#            0 1 2 3 4 5 6 7 8 9             
listaLeds = [6,2,5,5,4,5,6,3,7,6]
#### Inicio

qtdCasos = int(input())
for caso in range(0, qtdCasos):
  linha = input()
  totalLeds = 0
  for i in range(0, len(linha)):
    #print(f"O numero {linha[i]} tem {listaLeds[int(linha[i])]} leds")
    totalLeds += listaLeds[int(linha[i])]

  print(f"{totalLeds} leds")


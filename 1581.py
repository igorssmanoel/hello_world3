casos = int(input())

for caso in range(casos):
  qtd_idiomas = int(input())
  idioma_anterior = input()
  idioma_nativo = True
  for vez in range(qtd_idiomas-1):
    idioma = input()
    if (idioma_anterior != idioma):
      idioma_nativo = False
      
  if (idioma_nativo):
    print(idioma_anterior)
  else:
    print("ingles")

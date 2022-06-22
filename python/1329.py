while input() != '0':
  pontuacoes = list(map(int, input().split()))
  dicionario = {"Mary": 0, "John": 0}
  
  for pontuacao in pontuacoes:
    if pontuacao == 0:
      dicionario["Mary"] += 1
    else:
      dicionario["John"] +=1

  print(f"Mary won {dicionario['Mary']} times and John won {dicionario['John']} times")
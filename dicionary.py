dicionario = {
  "igor": {
    "idade": 28
  },
  "weyner": {
    "idade": 63
  }
}

print(dicionario.get("igor"))  # Retorna o valor do dicionario pela chave
""" print(dicionario["igorx"]) """

print(dicionario)

dicionario["ricardo"] = {"idade": 40}

print(dicionario)

dicionario.pop("igor")

print(dicionario)

print(dicionario.keys())
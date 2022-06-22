""" teste = "Igor Manoel".split()
teste.append(len(teste))
print(teste) """


class MyStr:
  def __init__(self, string):
    self.string = string
  
  def split(self, separador=" "):
    string_splitada = self.string.split(separador)
    string_splitada.append(len(string_splitada))
    return string_splitada

teste = MyStr("Igor Manoel")
print(teste.split())
from datetime import datetime

def leNome():
  return input("Digite o seu nome: ")

def leCpf():
  return input("Digite o seu cpf: ")

def leNascimento():
  return input("Digite a data de nascimento no formato xx/xx/xxxx: ")

def calculaIdade(nascimento):
  dataAtualTimestamp = datetime.now().timestamp()
  nascimentoTimestamp = datetime.strptime(nascimento, '%d/%m/%Y').timestamp()

  diffTimestamp = dataAtualTimestamp - nascimentoTimestamp
  
  result = int(diffTimestamp/60/60/24/365.25)

  return result


nome = leNome()
cpf = leCpf()
nascimento = leNascimento()
idade = calculaIdade(nascimento)

print(f"Nome: {nome}  cpf: {cpf}  idade: {idade} anos")


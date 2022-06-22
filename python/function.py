
from datetime import datetime, date

def horaAtual():
  return (datetime.now().strftime("%H:%M"))

def hoje():
  return (date.today().strftime("%d/%m/%Y"))

def dia():
  return (date.today().strftime("%d"))

hora = horaAtual()
data=  hoje()
dia_hoje = dia()

print(hora, data, dia_hoje)


def soma(a, b):
  return a + b

print(f"a soma dos numeros eh {soma(31, 59)}")
print(f"a soma dos numeros eh {soma(1, 1)}")
print(f"a soma dos numeros eh {soma(2, 5)}")
print(f"a soma dos numeros eh {soma(3, 0)}")


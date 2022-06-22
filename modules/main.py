import hellomodule
from hellomodule import hello_world
from hellomodule import hello_world as hw

print(hellomodule.hello())
print(hellomodule.world())
print(hellomodule.hello_world())

print(hello_world())
print(hw())



from statistics import * # Importa todos modules de statistica
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20



import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, Raiz quadrada
print(math.pow(2, 3))    # 8.0, Exponencial
print(math.floor(9.81))  # 9, Arredondar para baixo
print(math.ceil(9.81))   # 10, Arredondar para cima
print(math.log10(100))   # 2, Logaritmo com base 10



from math import pi
print(pi)

from math import pi as  PI
print(PI) # 3.141592653589793


import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
import random

x = 0
lista = []

while len(lista) < 10 :
    x = random.randint(-10,10)
    if x < 0 :
        x = 0
        lista.append(x)
    else :
        lista.append(x)
print(lista)
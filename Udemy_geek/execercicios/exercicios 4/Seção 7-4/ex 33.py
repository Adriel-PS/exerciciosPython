from random import randint

lista = []

while len(lista) < 10 :
    x = randint(0,10)
    lista.append(x)

backup = lista.copy()
lista2 = []

while len(backup) > 0 :
    x = backup.pop()
    if x > 0 :
        lista2.append(x)
print(lista,len(lista))
print(lista2,len(lista2))
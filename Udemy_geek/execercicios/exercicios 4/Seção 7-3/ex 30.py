from random import randint

lista1, lista2 = [], []

while len(lista1) < 10 :
    x = randint(1,100)
    if x not in lista1 :
        lista1.append(x)

while len(lista2) < 10 :
    x = randint(1,100)
    if x not in lista2 :
        lista2.append(x)

lista1 = set(lista1)
lista2 = set(lista2)
iguais = lista2 & lista1
print(lista1)
print(lista2)
if len(iguais) > 0 :
    print(iguais)
else:
    print("sem iguais")
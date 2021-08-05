from random import randint

lista1 ,lista2 = [], []
todos = []
while len(lista1) < 10 :
    x = randint(1,20)
    if x not in lista1 :
        lista1.append(x)

while len(lista2) < 10 :
    x = randint(1,20)
    if x not in lista2:
        lista2.append(x)

lista1=set(lista1)
lista2=set(lista2)

todos=lista1.union(lista2)

print(lista1)
print(lista2)
print(todos)
print(len(todos))
import random

lista = []
rep = []
x , y = 0 , 0
while y < 20 :
    x=(random.randint(0,15))
    y+=1
    if x in lista :
       rep.append(x)
    else :
        lista.append(x)
lista.extend(rep)
print(lista)
print(rep)

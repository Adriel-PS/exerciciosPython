import random

lista = []
pos = []
neg = []
x = 0

while True:
    if x >= 10:
        break
    lista.append(random.randint(-10,10))
    x +=1

backup=lista.copy()

while True:
    x = lista.pop()
    if x >= 0 :
       pos.append(x)
    elif x < 0 :
        neg.append(x)
    if len(lista) == 0 :
        break
print(f"a lista original era {backup}")
print(f"a soma dos positivos é {sum(pos)}")
print(f"a quantidade de negativos é de {len(neg)}")
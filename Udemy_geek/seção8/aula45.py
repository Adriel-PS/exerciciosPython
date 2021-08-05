"""
função com retorno

numeros = [1, 2, 3, 4, 5]

def mostra():
    print(f"sao {len(numeros)} numeros ")
    print("e eles sao : ")
    print(numeros)
def linha():
    print("---------------------------------")

mostra()
numeros.pop()
linha()

def quadrado_de_7():
    print(7*7)
    #nao retorna apenas printa

quadrado_de_7()

def quadrado_de_9():
    return 9*9

x=quadrado_de_9()
print(x)
print(quadrado_de_9())


#retorno finaliza a função

def diz_oi():
    return "oi"

print(diz_oi())
def fun2():
    return "a","b","c","d"

a1,a2,a3,a4 = fun2()
print(a1,a2,a3,a4)
print(fun2())

"""

from random import *

def joga_moeda():
    valor = randint(1,2)
    if valor == 2 :
        return "cara"
    if valor == 1 :
        return "coroa"

i = 0

while(i < 5 ):
    print(f"jogada de numero {i+1} : {joga_moeda()} ")
    i=i+1
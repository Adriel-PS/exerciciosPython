"""
funçoes com parametros

-funções que recebem dados para ser usados dentro dela


-----------------------------------------------------------------------------------------------------------------------
def quadrado_de_7():
    return 7*7

print(quadrado_de_7())

def quadrado(numero):
    return numero*numero
    ## num **2
def linha():
    print("----------------------------")

linha()

x=int(input("informe x "))
y=int(input("informe y "))
z=int(input("informe z "))


print(f"o numero {x} ao quadrado é {quadrado(x)}")
print(f"o numero {y} ao quadrado é {quadrado(y)}")
print(f"o numero {z} ao quadrado é {quadrado(z)}")

def parabens(nome):
    print(f"parabens {nome}")

parabens("adriel")
parabens(input(str("diga o nome : ")))
"""



def soma(a, b) :
    return a + b

print(soma(2,2))


def soma_de_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total+num
    return total


lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

x = soma_de_impares(lista)
print(x)
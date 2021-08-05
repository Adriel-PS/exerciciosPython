from _collections import deque

lista = []
x,y,mult = 0,0,0
resultado = []

while len(lista) < 10 :
    y += 1
    lista.append(int(input(f"informe o numero {y}º na lista : ")))

print(lista)

mult = int(input("informe o numero q da multiplicação"))

while len(lista) > 0 :
    x = lista.leftpop()
    x = x * mult
    resultado.append(x)
resultado.reverse()
print(resultado)

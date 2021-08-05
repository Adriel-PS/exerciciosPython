import random
lista = []

while len(lista) < 5 :
    lista.append(random.randint(0,20))
print(lista)
codigo = int(input("informe 1 para mostrar na ordem original e 2 para inversao : "))
if codigo == 1 :
    print(f"orderm original {lista}")
elif codigo == 2 :
    lista.reverse( )
    print(f"lista inversa {lista}")
else :
    print("codigo invalido")
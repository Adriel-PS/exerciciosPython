lista = []
inverso = []
while True :
    x = int(input("informe um numero par "))
    if x%2 == 0 :
        lista.append(x)
        print("numero adicionado")
    else :
        print("o numero q vc informou nao é um numero par")
    if len(lista) == 6 :
        break
print(f"os numero sao {lista}")
while True :
    inverso.append(lista.pop())
    if len(lista) == 0 :
        break
print(f"os numero invertidos sao {inverso}")
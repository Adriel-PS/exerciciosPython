x=int(input("qual produto vc quer ?"))
y = int(input("qual a quantidade"))
produtos = [0,3,5,10]
valor = produtos[x] * y
print(f"valor é de {valor}")

lista = ["adriel", "hillary", "billy"]
lista2 = list(range(0, 101, 5))

# print(lista[])
# print(lista2[])

for cont in range(0, len(lista)):
    print(cont, lista[cont])

if "hillary" in lista:
    print("achei")
else:
    print("nao achei")

for num in range(1, 3):
    x = int(input("informe um numero a lista : "))
    lista.append(x)
print(lista)
lista.sort()
print(f"na sequncia é \n {lista}")

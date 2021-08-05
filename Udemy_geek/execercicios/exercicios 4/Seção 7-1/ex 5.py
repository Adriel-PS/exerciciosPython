lista = []
listapar = []
x = 0
valor = 4
while x < valor:
    lista.append(int(input(f"informe o {x+1}º : ")))
    x+=1

x = 0
while x < valor:
    if lista[x] % 2 == 0:
        listapar.append(lista[x])
    x+=1
print(f"os numeros foram \n{lista}\nos pares sao \n{listapar} com {len(listapar)} numeros")

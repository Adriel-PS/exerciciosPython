lista = []
x = 0
while True:
    if len(lista) >= 5:
        break
    x += 1
    lista.append(int(input(f"infome um {x}º numero: ")))
print(f"o maior numero esta na posição {lista.index(max(lista))}")
print(f"o maior numero esta na posição {lista.index(min(lista))}")

lista = []
x = 0
while True:
    if len(lista) >= 3:
        break
    x += 1
    lista.append(int(input(f"infome um {x}º numero  ")))
print(f"a lista é {lista}")
print(f"o maior numero é {max(lista)}")
a={max(lista)}
print(f"e o seu indice é {lista.index(max(lista))}")
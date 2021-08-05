lista = []
x = 0
while True:
    if len(lista) >= 5:
        break
    x += 1
    lista.append(int(input(f"infome um {x}º numero: ")))
print(f"a lista de numeros sao {lista}")
print(f"o maior é {max(lista)}")
print(f"o menor é {min(lista)}")

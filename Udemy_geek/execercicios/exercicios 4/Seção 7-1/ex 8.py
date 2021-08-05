lista = []
inversa = []
x = 0
while True:
    if len(lista) >= 6:
        break
    x += 1
    lista.append(int(input(f"infome um {x}º numero  ")))
print(lista)
while True:
    if len(lista) == 0:
        break
    inversa.append(lista.pop())
print(inversa)
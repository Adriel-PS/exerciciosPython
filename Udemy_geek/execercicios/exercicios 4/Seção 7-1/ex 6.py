lista = []
x = 0
while True:
    if len(lista) >= 10:
        break
    x += 1
    lista.append(int(input("infome um numero ")))
print(f"a lista é {lista}")
print(f"o menor numero é {min(lista)}")
print(f"o maior numero é {max(lista)}")

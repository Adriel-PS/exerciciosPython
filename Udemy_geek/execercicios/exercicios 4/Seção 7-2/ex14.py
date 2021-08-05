lista = []
l2 = []
x = 0
valor = 0
while True:
    if len(lista) >= 5:
        break
    x += 1
    valor=((int(input(f"infome um {x}º numero: "))))
    if valor in lista :
        l2.append(valor)
    lista.append(valor)
print(f"a lista é {lista}")
if len(l2) > 0 :
    print(f"e os numero repeitos sao {l2}")
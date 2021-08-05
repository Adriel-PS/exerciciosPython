lista = []
y = 0
while len(lista) < 10 :
    x = int(input("informe outro numero : "))
    y+=1
    if x not in lista :
        lista.append(x)
    else :
        print("este numero ja esta na lista , informe outro numero ")
lista.sort()
print(lista)


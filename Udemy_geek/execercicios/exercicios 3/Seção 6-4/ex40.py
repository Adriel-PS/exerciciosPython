rmaior= 0
rmenor=1000000
x=0
while True  :
    x = int(input("informe um numero caso seja negativo o programa ira fechar "))
    if x > 0 :
        if x > rmaior :
            rmaior = x
        if x < rmenor :
            rmenor = x

    else :
        break
print(f"o maior numero escrito foi {rmaior} \no menor numero escrito foi {rmenor}")
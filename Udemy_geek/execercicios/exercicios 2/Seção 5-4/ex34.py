print("informe sua nota e suas faltas ")
n=float(input("sua nota é : "))
f=int(input("sua quantidade de faltas : "))

if n >= 9.0 and n <= 10.0 :
    if f >= 20 :
        print("seu conceito é B")
    else :
        print("seu conceito é A")

elif n >= 7.5 and n <= 8.9 :
    if f >= 20 :
        print("seu conceito é C")
    else :
        print("seu conceito é B")

elif n >= 5.0 and n <= 7.4 :
    if f >= 20 :
        print("seu conceito é D")
    else :
        print("seu conceito é C")

elif n >= 4.0 and n <= 4.9 :
    if f >= 20 :
        print("seu conceito é E")
    else :
        print("seu conceito é D")

if n < 3.9 :
    if f >= 20 :
        print("seu conceito é E")
    else :
        print("seu conceito é E")
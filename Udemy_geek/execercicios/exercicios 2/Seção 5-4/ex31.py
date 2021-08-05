peso=int(input("informe seu peso : "))
altura=float(input("informe sua altura : "))
if altura < 1.20 :
    if peso <=60 :
        print("sua categoria é A")
    elif peso > 60 and peso <= 90 :
        print("sua categoria é D")
    else :
        print("sua categoria é G")
elif altura >= 1.20 and altura <= 1.70 :
    if peso <= 60 :
        print("sua categoria é B")
    elif peso > 60 and peso <= 90 :
        print("sua categoria é E")
    else :
        print("sua categoria é H")
elif altura >= 1.70 :
    if peso <= 60 :
        print("sua categoria é C")
    elif peso > 60 and peso <= 90 :
        print("sua categoria é F")
    else :
        print("sua categoria é i")


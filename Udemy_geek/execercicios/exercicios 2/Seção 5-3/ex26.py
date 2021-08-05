km=int(input("qual o quantidade de kilometros por litro seu carro faz ? : "))
if km < 8 :
    print("venda o carro")
elif km > 8 and km < 12 :
    print("economico ")
elif km >= 12 :
    print("super econimico")
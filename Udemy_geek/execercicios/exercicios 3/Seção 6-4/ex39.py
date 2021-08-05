base=0
altura =0
area = 0
conf="sim"
x=0
while True :

   

    while base <= 0 :
        base = int(input("informe um valor valido para a base do triangulo : "))

    while altura <= 0 :
        altura = int(input("informe um valor valido para a base do triangulo : "))

        area = (base*altura)/2
        print(f"a area do quadrado é de {area}" )


print("ok ate mais")
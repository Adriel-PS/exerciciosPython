quadrado,cubo,raiz=0,0,0
while True :
    x = int(input("informe um numero "))
    if x <= 0 :
        break
    quadrado = x*x
    cubo = x*x*x
    raiz = x**0.5
    print(f"{x} elevado ao quadrado é {quadrado} , elevado ao cubo {cubo} e sua raiz quadrada é {raiz}.")
print("fim do programa")
#exercio com tipo float
x=float(input("informe um numero " ))
if x > 0 :
    num=(x**0.5)
    print("a raiz desse numero é ",num)
elif x < 0 :
    num=(x*x)
    print("o numero ao quadrado é",num)
else:
    print("nao é possivel fazer raiz e nem potencia com 0")
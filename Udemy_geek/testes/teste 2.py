print("calculando (a²=b²+c²)")
x=str(input("qual o x da questão ?"))
if x == "a":
    b=int(input("informe b"))
    c=int(input("informe c"))
    a=(b*b)+(c*c)
    a=float(a**0.5)
    print(a)
elif x == 'b':
    a=int(input("informe a"))
    c=int(input("informe c"))
    b=(a*a)-(c*c)
    b=float(b**0.5)
    print=("o resultado é",b)
elif x == 'c':
    a=int(input("informe a"))
    b=int(input("informe b"))
    c=(a*a)-(b*b)
    c=float(c**0.5)
    print=(c)
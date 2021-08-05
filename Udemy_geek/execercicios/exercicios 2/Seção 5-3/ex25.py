print("equação de segundo grau ax²+bx+c=0(lembrando que a nao pode ser menor q 0 ")
a=int(input("informe a "))
if a == 0 :
    print("nao é equação de segundo grau")
b=int(input("informe b "))
c=int(input("informe c "))
delta=(b**2)-4*a*c
b2=b-(b*2)
print(f"delta é igual a {delta}")
if delta < 0 :
    print("nao existe raiz real")
elif delta == 0:
    print(f"existe apenas uma raiza")
    x1 = b2 + (delta ** 0.5) / (2 * a)
    print(x1)
elif delta > 0:
    print("existe 2 raizes")
    x1 = b2 + (delta ** 0.5) / (2 * a)
    x2 = b2 - (delta ** 0.5) / (2*a)
    print(x1)
    print(x2)

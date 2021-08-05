import sys
print("informe 3 numeros positivos e maior q zero  ")
x=int(input("informe x : "))
if x <= 0 :
    print("refaça com um numero positivo e maior q zero")
    sys.exit()
y=int(input("informe y : "))
if y <= 0 :
    print("refaça com um numero positivo e maior q zero")
    sys.exit()
z=int(input("informe z : "))
if z <= 0 :
    print("refaça com um numero positivo e maior q zero")
    sys.exit()
geometrica=(x*y*z)*1/3
ponderada= (x+2*y+3*z)/6
harmonica=1/(1/x+1/y+1/z)
aritimetica=x+y+z/3
print(f"os resultado de cada conta sao: \ngeometrica {geometrica} \npoderada {ponderada} \nharmonica {harmonica}\naritimetica {aritimetica}")

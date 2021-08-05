vezes=int(input("informe quantos numeros sao : "))
i,r=0,0
while vezes > i :
    x=int(input(f"informe o numero de {i+1}/{vezes} "))
    i=i+1
    r=r+x
print(r)
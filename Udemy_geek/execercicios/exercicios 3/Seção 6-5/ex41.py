r1,r2=0,0
res=1
while True :
    r1 =int(input("informe o primeiro valor"))
    if r1 == 0 :
        break
    r2=int(input("informe o primeiro valor"))
    if r2 == 0 :
        break
    res = (r1*r2)/(r1+r2)
    print(f"o resultado é de {res}")
print("fim do programa")
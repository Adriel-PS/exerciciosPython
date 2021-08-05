dv11=0
dv13=0
dv17=0
num = int(input("informe um numero : "))
for n in range (num,num+17) :
    if n % 11 == 0 :
        dv11=n
    if n % 13 == 0 :
        dv13=n
    if n % 17 == 0 :
        dv17=n
print(f"o multiplos apartir de {num} sao {dv11} {dv13} {dv17}")
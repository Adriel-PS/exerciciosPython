num = int(input("informe um numero inteiro e positivo : "))
y=1
h=0
soma =0
for x in range (1,11) :
    y=y*2
    h=num/y
    print(f"{num}/{y} é {h} ")
    soma = soma + h
print(soma)
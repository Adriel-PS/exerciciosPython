soma = 0
ps = 0
a=0
for num in range(10) :
    ps = int(input(f"escreva o numero {num+1}/10 : "))
    if ps >= 0 :
        soma = soma + ps
        a=a+1
resultado = soma/a
print(f"o media é de {resultado}")

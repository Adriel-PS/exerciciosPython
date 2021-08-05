from random import randrange, uniform
#print(randrange(0, 9)) #faixa de inteiro
#print(uniform(0, 9)) #faixa de ponto flutuante

x=randrange(1,100)
num = int(input("informe numero "))
while num != x :
    if num > x :
        print(f"o numero é menor {num}")
        num = int(input("informe outro numero "))
    if num < x :
        print(f"o numero é maior {num}")
        num = int(input("informe outro numero "))
    if num == x :
        break
print(f"acertou o numero é {x}")
x=int(input("quantas somas sao ? "))
y=x
x=x+1
soma = 0
for n in range (1,x) :
    soma = soma + int(input(f"qual a soma {n}/{y} : "))
print(f"o resultado é {soma}")
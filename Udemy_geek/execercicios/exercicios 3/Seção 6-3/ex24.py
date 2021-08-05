x=int(input("informe um numero inteiro positivo : "))
m=0
for num in range (1,x,1):
    if x % num == 0 :
        print(f"{x} é divisivel por {num}")
        m=m+num
print(f"a soma dos divisores de {x} é de {m}")
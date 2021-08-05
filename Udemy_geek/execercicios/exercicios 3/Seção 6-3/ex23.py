x=int(input("informe um numero inteiro positivo : "))
for num in range (1,x,1):
    if x % num == 0 :
        print(f"{x} é divisivel por {num}")

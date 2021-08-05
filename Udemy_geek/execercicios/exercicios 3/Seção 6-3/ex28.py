import math

x=int(input("informe um numero "))
for num in range (1,x+1):
    x=math.factorial(num)
    soma = num/x
    print(f"1/{num}! ({num}/{x}) = {soma} ")



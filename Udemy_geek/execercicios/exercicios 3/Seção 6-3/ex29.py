import math

num2=0
soma=1
x = int(input("informe o numero : "))
for num in range(1,x+1):
    num2=num*2
    fac=math.factorial(num2)
    print(f"{num}/{num2}! {fac}")
    soma=soma+(num/fac)
print(f"o resultado é {soma}")
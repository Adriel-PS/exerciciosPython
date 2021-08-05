print("primeira parte")
n=0
soma = 0
x = int(input("informe o algoritmo limite : "))
for num in range (1,x+1):
    print(num)
    soma=soma+num
print(f"o resultado é {soma}")


print("segunda parte")
x = int(input("informe o algoritmo limite : "))
soma=0
for num in range (1,x+1):

    if num % 2 == 0 :
        soma=soma-num
        print(f"-{num}")
    elif num % 2 == 1 :
        soma = soma + num
        print(f"+{num}")
print(f"o resultado é {soma}")


print("terceira parte")
soma=0
x = int(input("informe o algoritmo limite : "))
for num in range (1,x+1,2):
    print(num)
    soma=soma+num
print(f"o resultado é {soma}")
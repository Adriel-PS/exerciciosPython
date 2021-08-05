x=0
maior=0
menor=10
for num in range (1,11) :
    x=int(input(f"informe o numero {num}/10 : "))
    if x > maior :
        maior = x
    elif x < menor :
        menor = x
print(f"o maior é {maior} e menor é {menor}")
soma = 0
print("calculo da media de 10")
for num in range(10) :
    soma = soma + int(input(f"vamos calcula a media , digite o numero {num+1}/10 : "))
soma = soma/10
print(f"a media é {soma}")
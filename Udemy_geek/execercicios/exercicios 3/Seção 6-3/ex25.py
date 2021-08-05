soma = 0
for num in range (1,1000,1):
    if num % 3 == 0 or num % 5 == 0 :
        soma = soma + num
print(soma)
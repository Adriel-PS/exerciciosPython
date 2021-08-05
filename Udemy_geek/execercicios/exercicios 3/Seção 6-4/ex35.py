x = int(input("informe o valor inicial "))
y = int(input("informe o valor final "))
soma =0

if x > y :
    print("informe um valor valido")

for num in range (x,y):
    if num % 2 == 1 :
        soma = soma+num
print(f"a soma dos numeros impares no intervalo é de {soma}")
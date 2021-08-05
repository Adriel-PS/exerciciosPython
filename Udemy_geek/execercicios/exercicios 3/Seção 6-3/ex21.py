x = int(input("informe o primeiro numero : "))
y = int(input("informe o segundo numero : "))
numn : 0
z1=0
z2=1

# algoritmo para garantir q o x seja o maior
if y < x :
    numn = y
    y = x
    x = numn

# para caso o x seja par
if x%2 == 0 :
    for num in range (x,y+1,2) :
        z1 = z1 + num

    for num in range (x+1,y+1,2) :
        z2= z2 * num


# para caso o x seja impar
elif x % 2 == 1:
    for num in range(x-1, y+1, 2):
        z1 = z1 + num

    for num in range(x, y+1, 2):
        z2 = z2 * num

print(f"a soma dos numeros pares sao de {z1} e a multiplicação dos numeros impares sao {z2}")
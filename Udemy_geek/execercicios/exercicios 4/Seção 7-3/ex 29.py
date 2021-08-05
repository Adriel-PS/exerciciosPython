from random import randint

numeros, pares, impares = [], [], []

while len(numeros) < 6 :
    x = randint(0,20)
    if x not in numeros :
        numeros.append(x)

backup=numeros.copy()
backup.reverse()

while len(backup) > 0 :
    x = backup.pop()
    if x % 2 == 0 :
        pares.append(x)
    else :
        impares.append(x)

print(f"lista é {numeros}")
print(f"os pares sao {pares} e a soma deles é de {sum(pares)}")
print(f"os impares sao {impares} e a quantidade é de {len(impares)}")

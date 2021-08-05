n = int(input("informe a quantidade de deseja : "))
i = int(input("informe um valor "))
j = int(input("informe um segundo valor "))
aux= 0
contador=0

while True :
    if aux % i == 0 or aux % j == 0 :
        print(aux)
        contador += 1
    aux += 1
    if contador == n :
        print("fim")
        break
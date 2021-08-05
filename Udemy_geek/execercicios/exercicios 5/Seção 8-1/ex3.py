def ver_negativo(num):
    if num > 0 :
        return 1
    elif num < 0 :
        return -1
    else:
        return 0

x = int(input("informe um numero: "))
print(ver_negativo(x))
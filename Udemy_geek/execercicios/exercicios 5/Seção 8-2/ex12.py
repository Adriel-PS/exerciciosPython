def conta(num):
    num1 = 0
    num2 = 0
    num3 = 0

    lista = (list(num))
    tamanho = len(lista)
    marcador = True

    numReal = int(num)
    if numReal <= 0:
        print("conta nao valida")
        marcador = False
        return "operação invalida"

    if tamanho == 1 and marcador:
        num1 = int(lista[0])
        num2 = 0
        num3 = 0
    elif tamanho == 2 and marcador:
        num1 = int(lista[0])
        num2 = int(lista[1])
        num3 = 0
    elif tamanho == 3 and marcador:
        num1 = int(lista[0])
        num2 = int(lista[1])
        num3 = int(lista[2])

    resultado = num1+num2+num3
    return f"o resultado é {resultado}"

x = str(input("informe um numero: "))
print(conta(x))

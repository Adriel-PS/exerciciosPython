def maior_que(num1,num2):
    if num1 > num2 :
        return f"o numero {num1} é maior que {num2}"
    elif num2 > num1:
        return f"o numero {num1} é maior que {num2}"
    else:
        return f"ambos numero são iguais"

while True:
    conf = int(input("digite qualquer numero para começar , para terminar digite 0"))
    if conf == 0 :
        print("fim")
        break
    x = int(input("informe um numero: "))
    y = int(input("informe um segundo numero: "))
    print(maior_que(x, y))


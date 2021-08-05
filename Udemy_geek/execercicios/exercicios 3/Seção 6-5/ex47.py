print("informe a operação sendo que :  "
                  "\n1 para soma"
                  "\n2 para subtração"
                  "\n3 para multiplicação "
                  "\n4 para divisao"
                  "\n5 para finalizar o programa "
                  "\n : ")

while True :
    x = int(input("qual sua escolha ? : "))

    if x == 1 :

        print("vc escolheu adição ")
        num1 = int(input("informe o primeiro numero :"))
        num2 = int(input("informe o segundo numero :"))
        r=num1+num2
        print(f"a resposta é {r}")

    elif x == 2:

        print("vc escolheu subtração ")
        num1 = int(input("informe o primeiro numero :"))
        num2 = int(input("informe o segundo numero :"))
        r = num1 - num2
        print(f"a resposta é {r}")

    elif x==3:

        print("vc escolheu multiplicação ")
        num1 = int(input("informe o primeiro numero :"))
        num2 = int(input("informe o segundo numero :"))
        r = num1 * num2
        print(f"a resposta é {r}")

    elif x==4:

        print("vc escolheu divisao  ")
        num1 = int(input("informe o primeiro numero :"))
        num2 = int(input("informe o segundo numero :"))
        r = num1 / num2
        print(f"a resposta é {r}")

    elif x==5 :
        print("ok programa ira finalizar ")
        break
    else :
        print("escolja uma opção valida")
print("obrigado volte sempre")
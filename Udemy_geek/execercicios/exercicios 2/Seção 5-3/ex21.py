alt=str(input("escolha uma das opções abaixo "
              "\n 1 - soma entre 2 numeros"
              "\n 2 - diferença entre 2 numeros (maior pelo menor)"
              "\n 3 - produto entre 2 numeros "
              "\n 4 - divisao entre divisoes entre 2 numeros (o denominador nao pode ser 0)\n "))

if alt == "1" :
    num1=int(input("digite o primeiro numero : "))
    num2=int(input("digite o segundo numero : "))
    r=num1+num2
    print(f"o resutado da soma é {r}")

elif alt == "2" :
    num1=int(input("informe o primeiro numero : "))
    num2=int(input("informe o segundo numero : "))
    r = num1 - num2
    print(f"a diferença entre os numero sao de {r}")

elif alt == "3" :
    num1=int(input("informe o primeiro numero : "))
    num2=int(input("informe o segundo numero : "))
    r = num1 * num2
    print(f"o resultado é de {r}")

elif alt == "4" :
    num1=int(input("informe o primeiro numero (nao pode ser negativo) : "))
    if num1 > 0 :
        num2=int(input("informe o segundo numero : "))
        r=num1/num2
        print(f"o resultado é {r}")
    else :
        print("refaça com um numero maior q 0")

else :
    print(" refaça com uma respota valida")
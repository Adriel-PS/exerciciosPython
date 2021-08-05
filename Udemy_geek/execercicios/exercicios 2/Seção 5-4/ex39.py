salario=int(input("informe o valor do salario "))
tempo=int(input("informe o tempo de empresa "))
if salario <= 500 :
    salario=salario*1.25

elif salario <= 1000 :
    salario = salario*1.2

elif salario <= 1500 :
    salario = salario *1.15

elif salario <= 2000 :
    salario = salario*1.1

elif salario > 2000 :
    salario = salario

if tempo < 1 :
    print(salario)

elif tempo >=1 or tempo <= 3 :
    salario = salario + 100
    print(salario)

elif tempo >= 4 or tempo <= 6 :
    salario = salario+200
    print(salario)

elif tempo >= 7 or tempo <= 10 :
    salario = salario + 300
    print(salario)

elif tempo > 10 :
    salario = salario + 500
    print(salario)
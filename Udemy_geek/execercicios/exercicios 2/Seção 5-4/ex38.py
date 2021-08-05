dia = int(input("qual dia vc nasceu ?"))
mes = int(input("qual mes ? "))
ano = int(input('qual ano '))

#calculo para calcular ano bisesto com saida em true e false
p4=ano%4
p400=ano%400
p100=ano%100
if p4 == 0 or p400 == 0 :
    if p100 == 0 :
        bisesto=False
    else:
        bisesto=True
else:
    bisesto=False


if mes%2 == 1 :
    if dia >= 1 and dia <=31 :
        print("sua data de nascimento é valida")
    else :
        print("sua data de nascimento é invalida ")


elif mes%2 == 0 and not mes == 2 :
    if dia >= 1 and dia <=30 :
        print("sua data de nascimento é valida")
    else :
        print("sua data de nascimento é invalida ")


elif mes == 2 :
    if bisesto == True :
        if dia >= 1 and dia <= 29:
            print("sua data de nascimento é valida")
        else:
            print("sau data de nascimento é invalida ")
    else :
        if dia >= 1 and dia <= 28:
            print("sua data de nascimento é valida")
        else:
            print("sau data de nascimento é invalida ")

elif mes > 12 :
    print(" sua data de nascimento é invalida")
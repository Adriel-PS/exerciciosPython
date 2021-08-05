sexo=str(input("informe seu sexo , m para mulher e h para homem : \n"))
altura=float(input("informe sua altura \n"))
if sexo == 'h' :
    peso=(72.7*altura)-58
    peso2=str(peso)
    print("o seu peso ideal é de ",peso2[0:2])
elif sexo == 'm' :
    peso = (62.1 * altura) - 44.7
    peso2 = str(peso)
    print("o seu peso ideal é de ", peso2[0:2])
else :
    print("refaça com sexo valido")
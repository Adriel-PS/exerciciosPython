num=("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove",
     "dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete",
     "dezoito","dezenove","vinte")

while True :
    x = int(input("informe um numero de 0 a 20 : "))

    if x > 20 or x < 0 :
        print("refaça usando um numero valido, ",end=" ")
    else :
        break
print(f"seu numero é {num[x]}")
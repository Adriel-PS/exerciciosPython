"""x=0
lista = [12,13,8,5]
while True :
    x = str(input("digitar umn numero ? "))
    if x == "sim" :
        lista.append(int(input("infome o numero ")))
    else :
        break
print(lista)
lista2=lista.sort()
lista3=lista.count()
print(f"os numeros digitados foram {lista} "
      f", que sao um total de {lista.count()} algoritimos ,"
      f"e em ordem ficam {lista3}")"""

x=int(input())
lista=[]
num1=1
for num in range (x):
      num=input(f"informe algo do valor {num1} : ")
      num1+=1
      lista.append(num)
print(lista)
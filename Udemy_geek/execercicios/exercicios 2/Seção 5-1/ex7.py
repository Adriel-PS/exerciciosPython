num1=int(input("informe um numero : "))
num2=int(input("informe um segundo numero : "))
if num1 > num2 :
    x=num1-num2
    print("o maior numero é ",num1, "e a diferença é de ",x)
elif num2 > num1 :
    x = num2 - num1
    print("o maior numero é ", num2, "e a diferença é de ", x)
else :
    print("ambos tem o mesmo valor")
num1=int(input("informe o valor 1 : "))
num2=int(input("informe o valor 2 : "))
num3=int(input("informe o valor 3 : "))
if num1 > num2 and num1 > num3 :
    if num2 > num3 :
        print(f"a sequencia é de {num1} {num2} {num3}")
    else :
        print(f"a sequencia é de {num1} {num3} {num2}")
elif num2 > num1 and num2 > num3 :
    if num1 > num3 :
        print(f"a sequencia é de {num2} {num1} {num3}")
    else :
        print(f"a sequencia é de {num2} {num3} {num1}")
elif num3 > num1 and num3 > num2 :
    if num1 > num2 :
        print(f"a sequencua é de {num3} {num1} {num2}")
    else :
        print(f"a sequencia é de {num3} {num2} {num1}")
elif num1 != num2 or num1 != num3 or num3 != num2 :
    num12=num1 #n1 e n2 != n3
    num23=num2 #n2 e n3 != n1
    num31=num3 #n3 e n1 != n2
    if num12 > num3:
        print(f"a sequencia é de {num12} {num12} {num3}")
    elif num3 > num12 :
        print(f"a sequencua é de {num3} {num12} {num12}")
    if num23 > num1:
        print(f"a sequencia é de {num23} {num23} {num1}")
    elif num1 > num23 :
        print(f"a sequencua é de {num1} {num23} {num23}")
    if num31 > num2:
        print(f"a sequencia é de {num31} {num31} {num2}")
    elif num2 > num31 :
        print(f"a sequencua é de {num2} {num31} {num31}")
else :
    print(f"todos tem o mesmo valor :{num1} ")

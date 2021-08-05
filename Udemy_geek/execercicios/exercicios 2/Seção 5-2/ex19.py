num=int(input("informe o numero : \n"))
por5=num%5
por3=num%3
if por3 is por5 == 0:
    print("o numero é divisel por 3 e 5")
elif por5 == 0 :
    print("o numero é divisivel por 5")
elif por3 == 0 :
    print("o numero é divisivel por 3")
else :
    print("o numero nao é divisivel por 3 e 5")

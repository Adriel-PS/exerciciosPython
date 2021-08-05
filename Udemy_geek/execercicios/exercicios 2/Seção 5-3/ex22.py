idade=int(input("informe a sua idade "))
tr=int(input("informe o seu tempo de trabalho"))
if idade >= 65 :
    print("vc ja pode se aposentar")
elif tr >= 30 :
    print("vc ja pode se aposentar")
elif idade >= 60 and tr >= 25 :
    print("vc ja pode se aposentar")
else :
    print("vc ainda nao pode se aposentar")
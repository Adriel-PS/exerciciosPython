nome=str(input("qual se nome :"))
print(f"{nome}, vc ira fazer uma prova de soma")
n1=int(input("quanto é 13+25? "))
n2=int(input("quanto é 7 + 8? "))
n3=int(input("quanto é 71 + 9? "))
n4=int(input("quanto é 14 + 7? "))
n5=int(input("quanto é 9+9 ? "))
x=0
t1=t2=t3=t4=t5=False
if n1 == 28:
    x=x+2
    t1=True
if n2 == 15:
    x=x+2
    t2 = True
if n3 == 80:
    x=x+2
    t3 = True
if n4 == 21:
    x = x+2
    t4 = True
if n5 == 18 :
    x = x+2
    t5 = True
print(f"sua nota é {x}, vc acertou as seguintes questoes :")
if t1 == True :
    print ("a primeira")
if t2 == True :
    print ("a segunda")
if t3 == True :
    print ("a terceira")
if t4 == True :
    print ("a quarta")
if t5 == True :
    print ("a quinta")
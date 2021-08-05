primo = True
x=1

while True:
    num = int(input("informe o numero "))
    if num ==0 :
        break
    for n in range (2,num+1):
        if (num%n) == 0 :
            primo = False
            x+=1
    if x > 2 :
        print("nao é primo")
    else:
        print("é primo")
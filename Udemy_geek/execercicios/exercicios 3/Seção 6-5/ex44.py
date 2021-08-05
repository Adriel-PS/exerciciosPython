x1,x2,x3 = 1,1,0

num=int(input("informe um numero"))

print(x1,x2,end=" ")

while True :
    if x3 > num :
        break
    x3=x1+x2
    x1=x2
    x2=x3
    print(x3, end=" " )
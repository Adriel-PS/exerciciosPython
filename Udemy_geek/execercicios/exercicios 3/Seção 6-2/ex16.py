x=int(input("escolha um numero"))
if x//2 != 0 :
    x=x-1
    for num in range(x, 0, -2):
        print(num,end="")
else :
    for num in range (x,0,-2):
        print(num,end="")

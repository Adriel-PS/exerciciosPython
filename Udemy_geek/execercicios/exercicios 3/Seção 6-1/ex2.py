#while
x = 1
print('repetição usando while')
while x < 101 :
    print (x,"",end="")
    x=x+1
print("\n")

#do while
print("repetição usando do while ")
x=0
while True :
    x=x+1
    if x < 101:
        print(x,"",end="")
    else :
        break
print("\n")

#for
print("repetição usando for")
for num in range (1,101):
    print(num,"",end="")

x = int(input())
a = False
for num in range (2,x):
    print(x,"/",num)
    if x % num == 0 :
        a = True
        print("aqui")
if a == True:
    print("nao é primo")
else :
    print("é primo")
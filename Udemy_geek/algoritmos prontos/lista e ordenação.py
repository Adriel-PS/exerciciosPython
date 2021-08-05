x=[0,1,2,3,4,5,6,7,8,9,10]
for num in range (1,len(x)):
    x[num]=int(input(f"informe um numero que ser o {num}º da sequencia : "))
x.sort()
print(x)
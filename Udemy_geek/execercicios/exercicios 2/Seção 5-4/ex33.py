print("a ataualização é de "
      "\naté 50 é de 5%"
      "\nate 100 é de 10%"
      "\nacima de 100 é de 15%")

x=int(input("informe o valor do produto "))

if x <= 50 :
    x=x*1.05
    print(x)

elif x > 50 and x < 100 :
    x=x*1.10
    print(x)

elif x > 100 :
    x=x*1.15
    print(x)

r=str(input("quar saber o valor ? "))
if r == "sim" :
    if x <= 80 :
        print("barato")
    elif x > 80 and x < 120 :
        print('normal')
    elif x > 120 and x < 200 :
        print("muito caro ")
    else :
        print("muito caro")
else :
    print(" ok ")
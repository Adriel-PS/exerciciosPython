x=int(input("qual o valor da venda ?"))
if x >= 100000 :
    c=700+(x*0.16)
    c=str(c)
    print(c[0:5])
elif x < 100000 and x > 80000 :
    c = 650 + (x * 0.14)
    c = str(c)
    print(c[0:5])
elif x < 80000 and x > 60000 :
    c = 600 + (x * 0.14)
    c = str(c)
    print(c[0:5])
elif x < 60000 and x > 40000 :
    c = 550 + (x * 0.14)
    c = str(c)
    print(c[0:5])
elif x < 40000 and x > 20000 :
    c = 500 + (x * 0.14)
    c = str(c)
    print(c[0:5])
elif x < 20000 :
    c = 400 + (x * 0.14)
    c = str(c)
    print(c[0:5])
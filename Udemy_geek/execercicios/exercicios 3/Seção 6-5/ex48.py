x1,x2,x3,r = 1,1,0,0



while True :
    if x3 > 4000000 :
        break
    x3=x1+x2
    x1=x2
    x2=x3
    if x3 % 2 == 0 :
        r = r + x3
        print(r,x3)
print(r)
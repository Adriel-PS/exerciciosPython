import random
num=0
while num <= 100 :
    x = random.randint(0,10) #de 0 a 10
    y = random.randrange(0,10)#de 0 a 9
    num+=1
    print(f"{x} e {y}")

num=int(input())
p4=num%4
p400=num%400
p100=num%100

if p4 == 0 or p400 == 0 :
    if p100 == 0 :
        print("nao é bisesto")
    else :
        print("é bisesto")
else:
    print("nao é bisesto")
    
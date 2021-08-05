for x in range (1000,10000):
    a = str(x)
    b1 = a[0:2]
    b2 = a [2:4]
    c1 = int(b1)
    c2 = int(b2)
    c3 = c1 + c2
    c4 = c3*c3
    if c4 == x :
        print(x)
import sys
ld1=int(input("lado 1 : "))
ld2=int(input("lado 2 : "))
ld3=int(input("lado 3 : "))
s12=ld1+ld2
s13=ld1+ld3
s23=ld2+ld3
if ld1 > s23 or ld2 > s13 or ld3 > s12 :
    print("nao é um triangolo ")
    sys.exit()
if ld1 == ld2 == ld3 :
    print("é um triangolo equilatero")
elif ld1 == ld2 or ld2 == ld3 or ld3 == ld1 :
    print(" é um triangolo isoceles ")
elif ld1 != ld2 != ld3 :
    print("é um triangolo escaleno")
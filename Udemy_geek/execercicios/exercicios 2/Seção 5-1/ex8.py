import sys

nt1=float(input("informe o valor da nota"))
if nt1 < 10.0 and nt1 > 0 :
    ntv1=nt1
else :
    print("nota invalida")
    sys.exit()

nt2=float(input("informe o valor da nota"))
if nt2 < 10.0 and nt2 > 0 :
    ntv2=nt2
else :
    print("nota invalida")
    sys.exit()

media = (ntv1 + ntv2)/2
print(media)

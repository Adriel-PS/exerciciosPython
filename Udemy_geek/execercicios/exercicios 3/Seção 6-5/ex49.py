numc=750
numj=250
rc=0
rj=0
contador=0
while rj <= rc :
    rc=(numc)+(rc*1.02)
    rj=(numj)+(rj*1.05)
    contador += 1
    print(contador,"-",rj,"-",rc)
print(f"a quantidade de mes é de {contador}")
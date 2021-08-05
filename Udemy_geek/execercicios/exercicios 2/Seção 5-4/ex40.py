cf = int(input("informe o valor cf "))
if cf <= 12000 :
    cf = str(cf*1.15)
elif cf > 12000 or cf <= 25000 :
    cf = str(cf*1.25)
elif cf > 25000 :
    cf = str(cf * 1.35)
print(cf)

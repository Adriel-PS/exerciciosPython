a=[1,0,5,-2,-5,7]
print(f"os valor são {a}")
soma= 0
soma = (soma+a[0])
soma = (soma+a[1])
soma = (soma+a[5])
print(f"a soma dos itens 0,1,5 é {soma}")
a[4]=100
for posição,valor in enumerate(a) :
    print(f"o valor {posição} é {valor}")
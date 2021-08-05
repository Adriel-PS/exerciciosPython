salario = 2000
x=0.015
for num in range (1994,2020,1):
    salario = salario+(salario*x)
    x=x*2
    s=str(salario)
    print(s[0:10])
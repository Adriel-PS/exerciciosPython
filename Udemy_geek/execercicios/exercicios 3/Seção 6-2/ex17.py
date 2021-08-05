x=int(input("informe o primeiro valor"))
y=int(input("informe o segundo valor "))
soma1,soma2=0,0
for num1 in range (0,x+1,1):
    soma1 = soma1+num1
for num2 in range(0,y+1,1):
    soma2 = soma2+num2
total=soma1+soma2
print(f"o total é de {total}")
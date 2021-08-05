n100,n50,n20,n10,n5,n2,n1=0,0,0,0,0,0,0

x= int(input("informe o valor do saque : "))

while x >= 100:
    x=x-100
    n100+=1
while x >= 50:
    x=x-50
    n50+=1
while x >= 20:
    x=x-20
    n20+=1
while x >= 10:
    x=x-10
    n10+=1
while x >= 5:
    x=x-5
    n5+=1
while x >= 2:
    x=x-2
    n2+=1
while x >= 1:
    x=x-1
    n1+=1

print(f"Sao {n100} nota de 100"
      f"\nSao {n50} nota de 50"
      f"\nSao {n20} nota de 20 "
      f"\nSao {n10} nota de 10 "
      f"\nSao {n5} nota de 5"
      f"\nSao {n2} nota de 2"
      f"\nSao {n1} nota de 1")
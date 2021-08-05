n1 = 1
n2 = 1
n3 = 0
n = int(input("Digite um numero:"))

print(n1, n2, end=" ")

while True:
    if n3 >= n:
        break
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
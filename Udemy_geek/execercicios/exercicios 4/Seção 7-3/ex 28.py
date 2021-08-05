from random import randint

v, v1, v2 = [], [], []

while len(v) < 10 :
    x = randint(0,100)
    if x not in v :
        v.append(x)

backup=v.copy()
backup.reverse()

while len(backup) > 0 :
    x=backup.pop()
    if x % 2 == 0:
        v1.append(x)
    else :
        v2.append(x)

print(f"a lista {v}")
print(f"os numero pares {v1}")
print(f"os numero impares {v2}")
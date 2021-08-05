from random import randint

x, y = [], []
r1, r2, r3, r4, r5 = [], [], [], [], []

while len(x) < 5:
    num = randint(1, 20)
    if num not in x:
        x.append(num)
print(f"lista 1 {x} ")

while len(y) < 5:
    num = randint(1, 20)
    if num not in y:
        y.append(num)

print(f"lista 2 {y}")

xb = x.copy()
yb = y.copy()
xb = set(xb)
yb = set(yb)

a = int(0)
while True:
    soma = x[a]+y[a]
    r1.append(soma)
    if len(r1) >= 5:
        break
    a += 1
print(f"a soma é {r1}")

a = 0
while True:
    mult = x[a]*y[a]
    r2.append(mult)
    if len(r2) >= 5:
        break
    a += 1
print(f"a multiplicação é {r2}")

r3 = xb.difference(yb)
print(f"os itens q estao apenas no lista 1  {r3}")

r4 = xb.intersection(yb)
print(f"os itens q estao em ambos {r4}")


xc=set(x)
yc=set(y)

a = xc.difference(yc)
b = yc.difference(xc)
r5 = a.union(b)
print(f"os itens q estao em apenas uma das listas sao {r5}")


a = []
b = []
c = []
x = 1
while len(a) < 3:
    a.append(int(input(f"{x}º numero do a : ")))
    x += 1

x = 1
while len(b) < 3:
    b.append(int(input(f"{x}º numero do b : ")))
    x += 1

print('', a,"\n",b)

while len(b) > 0 :
    x = b.pop()
    x = x - a.pop()
    c.append(x)
c.reverse()
print(c)
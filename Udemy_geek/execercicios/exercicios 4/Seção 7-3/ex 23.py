alista, blista, rlista = [], [], []
x = 1
produto = 0

while len(alista) < 3 :
    alista.append(int(input(f"infomre o {x}º : ")))
    x+=1

x = 1
while len(blista) < 3 :
    blista.append(int(input(f"infomre o {x}º : ")))
    x+=1
x=0
while len(rlista) < 3 :
    a = int(alista[x])
    b = int(blista[x])
    re = a * b
    rlista.append(re)
    produto = produto + re
    x+=1
print(alista,blista,produto)

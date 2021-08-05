alista, blista, rlista = [], [], []
x = 1

while len(alista) < 10 :
    alista.append(int(input(f"infomre o {x}º : ")))
    x+=1
x = 1

while len(blista) < 10 :
    blista.append(int(input(f"infomre o {x}º : ")))
    x+=1

x=0

while len(rlista) < 10 :

    if len(rlista) % 2 == 0 :
        rlista.append(alista[x])
        x=+1
    if len(rlista) % 2 == 1 :
        rlista.append(blista[x])
        x=+1

print(rlista)
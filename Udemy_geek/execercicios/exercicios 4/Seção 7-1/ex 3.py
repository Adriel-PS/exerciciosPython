tabela1 = []
tabela2 = []
x = 0
y = 0
while True:
    if len(tabela1) >= 10:
        break
    x += 1
    tabela1.append(int(input(f"informe o numero {x}º : ")))

x = 0
print(tabela1)

while True:
    if len(tabela2) >= 10:
        break
    y = tabela1[x]*tabela1[x]
    tabela2.append(y)
    x += 1
print(tabela2)

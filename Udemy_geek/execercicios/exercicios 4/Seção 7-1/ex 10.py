lista = []
x=0
while True:
    if len(lista) >= 15:
        break
    x += 1
    lista.append(float(input(f"informe a nota do aluno {x}: ")))
geral=sum(lista)
geral=geral/15
print(f"a media é de {geral}")
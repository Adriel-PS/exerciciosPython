nota , r , media = 0,0,0

print("digite a nota dos aluno (caso queira parar digite -1)")

while True :
    nota = int(input(f"informe a nota do aluno {r+1} : "))
    if (nota >= 0 and nota <= 10):
        media = media + nota
        r=r+1
    elif (nota == -1):
        print("finalizando programa")
        break
    else :
        print("informe um nota valida")

media = media / r
print(f" a media é {media}")
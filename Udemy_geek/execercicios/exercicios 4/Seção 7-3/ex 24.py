alunos = []
while len(alunos) < 5:
    alunos.append(int(input("informe o numero ")))
x=max(alunos)
print(f"o maior aluno é o {alunos.index(x)} com {x} de altura")
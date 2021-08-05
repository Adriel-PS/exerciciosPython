tabela = []
x = 1
while x < 9:
    tabela.append(int(input(f"informe o {x}º : ")))
    x +=1
soma = tabela[int(input("informe uma posição de 1 a 8 : "))-1]
soma = soma + tabela[int(input("informe uma posição de 1 a 8 : "))-1]
print(f"o resultado da soma é de {soma}")
sl = float(input("informe o salario "))
em = float(input("informe o valor do emprestismo "))
psl = sl/5

if psl > em :
    print('emprestimo disponivel')
elif psl == em :
    print("emprestimo disponivel")
else :
    print("emprestimo indisponivel")
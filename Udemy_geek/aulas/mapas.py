receita = {'jan':100,'fev':150,'mar':200}

'''
print(receita.keys())
print(receita.values())

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])'''

for chave in receita.keys():
    print(f"{receita[chave]} é de {chave} ")

for chave, valor in receita.items():
    print(f"a chave: {chave} ,tem com valor {valor} ")

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
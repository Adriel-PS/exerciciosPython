"""

ordered dic

# dicionario a ordem nao é garantida
dicionario = {'a': 1 , 'b':2,'c':3,'d':4,'c':5}

print(dicionario)

for chave , valor in dicionario.items():
    print(f"chave={chave} : valor={valor}")

ordered dict é um dicionario q garda a ordem dos itens (chave e valor)

"""

from _collections import OrderedDict

dicionario = OrderedDict({'c':3,'d':4,'e':5,'a': 1 , 'b':2})
print(OrderedDict(dicionario))
for chave , valor in dicionario.items():
    print(f"chave={chave} : valor={valor}")
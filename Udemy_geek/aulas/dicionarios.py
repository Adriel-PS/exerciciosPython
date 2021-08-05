"""
dicionarios em pyhton ,
em outras linguagens sao conhecidos como mapas

          chave / valor      chave / valor
paises = {"br" : "brasil" , "eua" : "estados unidos"}

            #nao podem ter chaves repetidas


dicionario ={"a":1,"b":2}               # criação de dicionario metodo 1 e mais usual
dicionario = dict('a'=1,'b'=1)          # criação de dicionario metedo 2 menos usual
print(paises["br"])                     # (chave) maneira de acessar um valor é usando a chave
print(paises.get("br"))                 # (get) maneira de acessar um valor , caso nao encontrado retonar none
pais=paises.get("bra","nao encontrado") # (get) usando a virgula retonamos um valor especificado caso nao tenha a chave selecionada
print('br' in paises)                   # veridica se a chave esta no dicionario , nao veridica o valor
dicionario["abr"]=abril                 # adição de dados
dicionario.update(novo_dado)            # adição de novo dado / novo_dado = {"mai":maio}
dicionario.update({"mai":maio})         # adição de novo dado
dicionairo["mai"]=maioo                 # atualização de valor
dicionario.update({"maio":maio})        # atualiza valor , nao aciona caso seja a mesma chave 
dicionario.pop("fev")                   # exclui a chave selecionada no () , e retorna o valor da chave
del receita['fev']                      # exclui a chave selecionada no []
dicionario.clear()                      # esvazia a lista
d=dicionario.copy                       # copia o dicionario (deep copy) copia independente
d=dicionario                            # copia o dicionario (shallow copy) e as alterações feitas por um modifica o outro
dicionario = {}.fromkeys('a','b')       # cria um dicionario com cada chave sendo um valor interavel sendo a o valor de cada chave o valor aprensentado
dicionario = {}.fromkeys(['nome','idade','email'],'none')
                                        # cria um dicionario com varias chaves e os mesmo valores , caso nao tenha valor especificado ficam com valor none

"""

#forma mais comum
"""paises ={"br":"brasil","eua":"estados unidos"}
print(paises)
print(type(paises))"""

"""paises = dict(br="brasil",eua="estados unidos")
print(paises["br"])

pais=paises.get("bra","nao encontrado")
print(pais)"""


receita = {"jan":100,"fev":150,"mar":300}
receita["abr"]=450
novo_dado = {"maio":500}
receita.update(novo_dado)
receita["maio"]=550
receita.update({"maio":500})

print(receita)

dicionario = {}.fromkeys(['nome','idade','email'])
print(dicionario)
#dicionario.update(nome='adriel',idade=19,email="driel@gmail.com")
print(dicionario)


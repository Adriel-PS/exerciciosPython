"""
        # TEORICO

comjuntos = sets
representados com {}
nao possuem indicesse , logo é usado quando nao se nescessita dessa ferramenta
nao possuem intens duplicados , logo os itens repetidos sao ignorados sem acontecer um erro
sao mutaveis
duplicidade nao gera erro apenas é ignorada


        # PRATICO



conjunto = {1,2,3,"adriel,True}                 # criação de conjuntos , nao precisam ser o mesmo tipo de valor
conjunto.add()                                  # adiciona itens
conjunto.remove()                               # remove itens , caso nao tenha o item retorna erro
conjunto.discard()                              # remove itens , caso nao tenha o item nao retorna erro
novo  = conjunto.copy()                         # (deep copy) copia o conjunto de forma independe , alterações feitas em um nao modificam outro
novo  = conjunto                                # (shallow copy) copia o conjunto , alterações feitas em um altera outros
conjunto.clear()                                # zera o conjunto
todos = conjunto1.union(conjunto2)              # cria um terceiro conjunto com o dados de ambos, sem duplicidade
unicos = conjunto1 | conjunto2                  # cria um terceiro conjunto com o dados de ambos, sem duplicidade
ambos = conjunto1.intersection(conjunto2)       # cria um conjunto contendo apenas dados q esteja em ambos conjuntos
ambos2 = conjunto1 & conjunto2                  # cria um conjunto contendo apenas dados q esteja em ambos conjuntos
so = cj1.difference(cj2)                       # cria um conjunto com os itens q estao em um conjunto mas nao no outro


"""

se={1,2,3,4,5,5,4}
print(se)
print(type(se))
es={1,3,4,5,10,20,30,40}
"""if 3 in se :
    print('tem')
else :
    print('nao tem ')"""
se.add(6)
se.remove(6)
se.discard(5)

todos = se.union(es)
print(todos,"\n",se,"\n",es)

unicos = se | es
print(unicos)

ambos = se.intersection(es)
print(ambos)

ambos2 = se & es
print(ambos2)

so1 = se.difference(es)
so2 = es.difference(se)
print(so1,"\n",so2)

print(sum(todos))
print(max(todos))
print(min(todos))
print(len(todos))
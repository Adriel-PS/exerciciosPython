""""
modulo collections - counter

recebe um valor interavel , o valor é adicionado em um dicionario , vira a chave e o valor é quantas vezes aquele item
foi citado

res = Counter(lista)

"""

from collections import Counter

lista = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]

res = Counter(lista)

print(res)
print(type(res))

print(Counter("adriel pereira siqueira"))

texto = """
A Classe Tegetthoff, também chamada de Classe Viribus Unitis, foi uma classe de navios couraçados operados pela Marinha Austro-Húngara, composta pelo SMS Viribus Unitis, SMS Tegetthoff, SMS Prinz Eugen e SMS Szent István. Suas construções começaram antes da Primeira Guerra Mundial; os batimentos das quilhas das duas primeiras embarcações ocorreram em 1910, enquanto das últimas duas aconteceram em 1912. O Viribus Unitis, Tegetthoff e Prinz Eugen foram construídos pelos estaleiros da Stabilimento Tecnico Triestino em Trieste, enquanto Szent István foi construído pela Ganz-Danubius em Fiume, assim ambas as partes da monarquia dual da Áustria-Hungria se envolveram.

O Viribus Unitis foi comissionado na frota austro-húngara em dezembro de 1912, seguido pelo Tegetthoff em julho de 1913 e pelo Prinz Eugen em julho de 1914. Entretanto, os estaleiros da Ganz-Danubius eram muito menores do que aqueles da Stabilimento Tecnico Triestino, o que fez com que a construção do Szent István atrasasse, atraso este piorado pelo início da Primeira Guerra em julho de 1914, com o navio só sendo comissionado em dezembro de 1915. Isto foi muito tarde para que ele participasse do Bombardeio de Ancona, em que os outros três couraçados tomaram parte imediatamente depois da Itália ter declarado guerra contra a Áustria-Hungria em maio de 1915
"""


palavras = texto.split()

re=(Counter(palavras))

print(re.most_common(5))

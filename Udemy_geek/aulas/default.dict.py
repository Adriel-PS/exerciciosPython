"""

colletion default dict

ao usar um default dict quando dermos uma chave para ele nos entregar o valor ele retornara um valor default em vez
de um keyerror .
caso queira mostrar a chave que nao existe ela criara a chave e como valor ficara o default
"""

        #pratica

"""dicionario = {'curso': 'programação em python '}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro'])"""

from collections import defaultdict

dicionario = defaultdict(lambda:0)

print(dicionario)

dicionario["curso"]="programação em python"

print(dicionario)

print(dicionario["outro"])

print(dicionario)
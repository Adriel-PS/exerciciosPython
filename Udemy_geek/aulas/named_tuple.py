"""

colletions named tuple


tupla = (1,2,3,4)

print(tupla[1])
print(tupla[3])

named tuple : sao tuplas onde nome me amos a tupla e os paremetros
"""

from collections import namedtuple


# forma 1 declaração named tuple
cachorro = namedtuple('cachorro' , 'idade raça nome ')

# forma 2 declaração named tuple

cachorro = namedtuple('cachorro', 'idade , raca , nome')

# forma 2 declaração named tuple

cachorro = namedtuple('cachorro',['idade','raça','nome'])

billy = cachorro(idade=5,raça='pudle',nome="billy")
yang=  cachorro(idade=0.5,raça='vira-lata',nome="yang")

print(billy)
print(yang)

print(billy.nome,billy.idade)
print(yang.nome,yang.idade)



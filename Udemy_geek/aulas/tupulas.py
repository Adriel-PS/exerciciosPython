"""
tuplas sao representadas por () , mas nao tem necessariamente de ter ()
tupla3 = (3) # isso nao é considerado uma tupula e sim uma vareavel simples
tupla3 = (3,) # isso é considerado uma tupula


tupula = tuple(range(10))       # gera uma tupula com o range de 10
tupula=1,2,3                    # é considerado uma tupula
tupula=(1)                      # nao é considerado uma tupula
tupula=(1,)                     # é considerado uma tupula
num1,num2,num3=tupula           # desempacotamento de tupula (so funciona quando a quantidade de vareaveis é a quantidade de objetos na tupula
print(sum(tupulanum))           # soma
print(max(tupulanum))           # numero maior numero
print(min(tupulanum))           # menor numero
print(len(tupulanum))           # quantidades de valores
tupla1 = tupla1+tupla2          # tupulas sao imutaveis mas seu valores podem ser alterados
print(3 in tupula)              # retonar valor true caso tenha o tres na tupula
print(tupula[3])                # acessa o valor no indice indicado
print(tupula.index(3))          # retorna a posição do valor pedido
print(tupula.index(3,2))        # retorna a posição do valor pedido apartir do indice selecionado
"""


#pratico


"""tupla1=(1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

tupla2=1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

tupla3 = (3)
print(tupla3)
print(type(tupla3))

tupla4 = (4)
print(tupla4)
print(type(tupla4))

tupula = tuple(range(10))
print(tupula)

tupula = "oi" , "tchau"
n1,n2 = tupula
print(n1)
print(n2)

#concatenação

tupla1 = (1,2,3)
print(tupla1)

tupla2 = (-3,-2,-1)
print(tupla2)

print(tupla1+tupla2)

tupla1 = tupla1+tupla2
print(tupla1)

tupula=1,2,0
if 3 in tupula :
    print("esta")
else :
    print("nao esta")

tupula = (2,6,14,26)

for n in tupula :
    print(n)

for indice,valor in enumerate(tupula):
    print(indice,valor)
"""
tupula=("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
i=0
while i < len(tupula) :
    print(tupula[i])
    i+=1
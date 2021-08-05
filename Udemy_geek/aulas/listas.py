"""


#transformando lista em str
lista2=["programação", "em", "python"]  # o " " é para definir qual ira ser o caracter que ficara entre os objetos
curso=" ".join(lista2)
print(curso)


lista1=[1]
transformando str em lista      #transfora str em lista sepandado pelas
curso = " curso de python "     #espaços na palavra
curso.split()                   #da para selecionar o separador como (,) ou (.) etc
lista1.append([1,2,3])          # add um comjumto ou um valor unico
lista1.extend([4,5,6])          # add intens separadamente mas com quantidade acima de 1
lista.insert(0,0)               # insere um valor no lugar especificado
lista.sort()                    # ordena a lista do menor para o maior
print(len(lista))               # conta quantos objetos tem na lista
lista.reverse()                 # inverte a lista
lista2=lista.copy()             # copia a lista selecionada
lista.pop()                     # remove o ultimo objeto da lista() remove o objeto indicado (2) \alem de retonar o dado
lista.clear()                   # limpa a lista
print(lista.index())            # mostra o indice do valor selecionado no () por exemplo (2) (nome)
print(sum(listanum))            # soma
print(max(listanum))            # numero maior numero
print(min(listanum))            # menor numero
print(len(listanum))            # quantidades de valores
tupula=tuple(listanum)          # transforma lista em tupula
novalista.copy(lista)           # (deepcopy) copia a lista e elas sao idependentes uma da outra
num1,num2,num3=lista            # desempacotamento de lista (so funciona quando a quantidade de vareaveis é a quantidade de objetos na lista
novalista = lista               # (shallow copy) a modificação de uma altera ambas
lista=list(range(10))           # gera uma lista com range de 10
    """

"""lista = [1,2,3]
print(f"1 {lista}")
lista.append(4)
print(f"2 {lista}")
lista.extend([5,6,7])
print(f"3 {lista}")
lista.insert(0,0)
print(f"4 {lista}")

listanomes=["adriel","hillary","billy","vanusa","damiao","gabrielly"]

#print(lista.index(6))
x=listanomes.index("hillary")
print(x)

print(listanum)
print(f"soma dos numeros {sum(listanum)}")  # soma
print(f"maior numero {max(listanum)}")  # numero maior numero
print(f"menor numero {min(listanum)}")  # menor numero
print(f"quantidade de valores {len(listanum)}")  # quantidades de valores
"""



listanum = [2,4,7,13,16,21]

lista=list(range(10))
print(lista)


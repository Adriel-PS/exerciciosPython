"""
definição de função :
sao pequenos trechos que realizem funções especificas

ja ultilizadas :
- print()
- min()
- max()
-len()
"""


cores= ["azul","rosa","amarelo"]
def linha():
    print("--------------------------------------------")

def diz_oi():
    print("oi")

def diz_cores():
    for num in range(len(cores)):
        print(cores[num])
        linha()


mostra_cor = diz_cores

mostra_cor()
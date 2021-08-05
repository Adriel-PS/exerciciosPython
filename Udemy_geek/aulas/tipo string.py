"""
tipo string 
sempre q estiver entre aspas simples, duplas , simples triplas , duplas triplas  
"oi" 'oi' '''oi''' """"oi"""
""" """


nome = 'adriel'
nome2 = '''pereira'''
nome3 = "siqueira"
nome4 = """isso ae"""
print (nome,nome2,nome3,nome4)
print(type(nome),type(nome2),type(nome3),type(nome4))



#formas de pular linha
# usando \n ou aspas triplas
nome = 'adriel pereira siqueira'
print(nome)
nome2 = """adriel
pereira
siqueira"""
print (nome2)
nome3 = 'adriel \npereira \nsiqueira '
print(nome3)

print( )
print( )
print( )

#modificações
nome = 'adriel p siqueria'
print(nome)
print(nome.upper()) #tudo maiusculo          #upper
print(nome.lower()) #tudo minusculo          #lower
print(nome.title()) #iniciais maiusculas     #title
print(nome.split()) #forma de lista          #split
print(nome[0:7]) #printa so as letras selecionadas -a ultima selecionada # slice de string
print(nome[5]) #unica letra selecionada
print(nome[::-1]) #inverte
print(nome.replace("a",'i')) # substitui caracter #replace
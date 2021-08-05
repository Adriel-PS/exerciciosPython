#imput sempre dará string 

#tipo1
print("qual seu nome ? ")
nome = input()
print("eae",nome)

#tipo 2 versao 2
print("qual seu nome ? ")
nome = input()
print("eae %s " %nome )

#tipo 3 versao 3
print("qual seu nome ? ")
nome = input()
print("eae {0}".format(nome))

#tipo 4 versao 3.7
print("qual seu nome ? ")
nome = input()
print(f"eae {nome}")

#para ter a saida com interio basta

idade =int(input("qual sua idade ?"))
print(f"vc nasceu em {2020-idade}")
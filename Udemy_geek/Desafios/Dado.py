"""
esse é um programa simples para jogar dados
no qual apresenta o seguintes desafios :
    *quantidade de dados
    *numero de facces no dado
    *repetição
"""
import random

faces_dados = 0
numDados = 0

#
while(True):
    cont = str(input("deseja começar/continuar?"))

    if cont == "sim":

        #informando a quantidades de dados
        numDados = int(input("informe quantos dados serão"))

        #buscando face de dado unico
        if numDados > 1 :
            faces_dados = int(input("informe quantas face os dados teram: "))

        #buscando faces de multiplos dados
        if numDados == 1:
            faces_dados = int(input("informe quanto"))

        


    elif cont == "nao":
        print("Muito obriado pela preferencia. Volte sempre!!")
        break


    else:
        print("comando nao indentidicado")

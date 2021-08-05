print("peça seu pedido "
      "\n cahorro quente , custa =1.20 "
      "\n bauru simples , custa = 1.30"
      "\n bauro com ovo , custa = 1.50"
      "\n hamburguer , custa = 1.20"
      "\n cheeseburguer , custa  = 1.70"
      "\n suco , custa = 2.20"
      "\n refrigerante ,custa = 1.00")
print("qual seu pedido (um de cada vez)?")

hotdog=float(1.2)
bauro_s=float(1.3)
bauro_ovo=float(1.5)
hamburguer=float(1.2)
c_burguer=float(1.7)
suco=float(2.2)
refri=float(1)

p1=str(input("qual seu pedido ?"))
q1=float(input("qual a quantidade ? "))

if p1 == 'cachorro quente' :
    hotdog=hotdog*10
    r=(hotdog*q1)/10
    print(f" o valor é de {r} ")

elif p1 == 'bauro_s' :
    bauro_s = bauro_s*10
    r=(bauro_s*q1)/10
    print(f" o valor é de {r} ")

elif p1 == 'bauro_ovo' :
    bauro_ovo = bauro_ovo*10
    r=(bauro_ovo*q1)/10
    print(f" o valor é de {r} ")

elif p1 == 'hamburguer' :
    hamburguer=hamburguer*10
    r=(hamburguer*q1)/10
    print(f" o valor é de {r} ")

elif p1 == 'c_burguer' :
    c_burguer=c_burguer*10
    r=(hamburguer*q1)/10
    print(f" o valor é de {r} ")

elif p1 == 'suco' :
    suco=suco*10
    r=(suco*q1)/10
    print(f" o valor é de {r} ")

elif p1 == 'refri' :
    refri=refri*10
    r=(refri*q1)/10
    print(f" o valor é de {r} ")

else :
    print("escolha uma opção valida ")
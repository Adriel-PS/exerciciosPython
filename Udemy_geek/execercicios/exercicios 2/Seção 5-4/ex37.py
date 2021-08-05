print("tabela de preços por hora"
      "\n 1 e 2 hora - R$ 1,00 "
      "\n 3 e 4 hora - R$ 1,40 "
      "\n 5 ou mais  - R$ 2,00 ")
h=int(input("vc ficou quatas horas ?"))

if h > 1 :
      x=1
      if h > 2 :
            x=x+1
            if h > 3 :
                  x=x+1
                  if h > 4 :
                        x=x+1
                        if h == 5 :
                              print(" o valor é de 6,4")
                        if h > 5:
                              h=h-5
                              h=h*2
                              v=h+4.8
                              print(f" o valor é de {v}")
                  else :
                        print("o valor é de 4,80")
            else :
                  print("o valor é de 3,40")
      else:
            print("o valor é de 2")
else :
      print(" o valor é de 1")
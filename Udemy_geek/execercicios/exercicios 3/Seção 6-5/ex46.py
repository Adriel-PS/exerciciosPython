
while True:
    escolha = int(input("\n"
                        "digite 1 para converter km/h para mt/s \n"
                        "digite 2 para converter mt/s para km/h \n"
                        "digite 3 para sair \n "
                        "\n"))
    if escolha == 1:
        x = int(input("informe quantos km/h para fazer a conversao : "))
        r = x / 3.6
        print(f"a resposta é {r} metros por segundo ")


    elif escolha == 2:
        x = int(input("informe quantos mt/s para fazer a conversao : "))
        r = x * 3.6
        print(f"a resposta é {r} quilometros por hora ")



    elif escolha == 3:
        break

    else:
        print("esolha uma opção valida")
print("obrigao volte sempre")
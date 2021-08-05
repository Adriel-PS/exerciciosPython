import sys
cidade=str(input("digite a cidade (sp,rj,ms,mg): \n"))

if cidade == "sp" or cidade == 'mg' or cidade == 'rj' or cidade == 'ms' :
    valor = int(input("digite o valor : "))

    if cidade == "sp":
        im= ((valor / 100 ) * 12)
        total=im+valor
        print(f"o valor é de {valor} e o imposto é de {im} dando um total de {total}")
        sys.exit()

    elif cidade == "rj":
        im = ((valor / 100) * 15)
        total = im + valor
        print(f"o valor é de {valor} e o imposto é de {im} dando um total de {total}")

    elif cidade == "ms":
        im = ((valor / 100) * 8)
        total = im + valor
        print(f"o valor é de {valor} e o imposto é de {im} dando um total de {total}")


    elif cidade == "mg":
        im = ((valor / 100) * 7)
        total = im + valor
        print(f"o valor é de {valor} e o imposto é de {im} dando um total de {total}")

else :
    print("informe uma cidade valida")

x = str(input("informe uma data: "))
lista = (x.split("/"))

def data(dia,mes,ano):
    calendario = ({"01": "janeiro",
                   "02": "fevereiro",
                   "03": "março",
                   "04": "abril",
                   "05": "maio",
                   "06": "junho",
                   "07": "julho",
                   "08": "agosto",
                   "09": "setembro",
                   "10": "outubro",
                   "11": "novembro",
                   "12": "dezembro", })
    mes_longo = calendario[mes]
    return f"{dia} de {mes_longo} de {ano}"

print(data(lista[0],lista[1],lista[2]))


def cal_seg(sec,min,hrs):
    total = (hrs * 60 *60)+(min*60)+sec
    return total


hora = int(input("informe as horas:"))
mi = int(input("informe os minutos:"))
sec = int(input("informe os segundos: "))

print(f"o resultado é:")
print(f"{cal_seg(sec,mi,hora)} segundos")
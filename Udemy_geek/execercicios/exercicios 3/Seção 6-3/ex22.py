print("informe sua nota entre 10 e 20 ,"
    " caso seja maior q 20 ou menor q 10 o programa mostrar sua media e ira finalizar")

qt = 0
r = 0
media = 0

x = int(input("informe sua nota"))
while x >= 10 and x <= 20 :
    qt = qt+1
    r = r + x
    x = int(input("informe sua nota"))
    media = r/qt

print(f"a media é de {media}")
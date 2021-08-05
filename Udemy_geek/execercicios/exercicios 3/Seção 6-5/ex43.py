x,media,aux=0,0,0

while True :
    x=int(input("informe uma idade : "))
    if x == 0 :
        break
    if aux == 0:
        media=x
    aux +=1
    media = (media+x)/2
print(f"a media é de {media}")
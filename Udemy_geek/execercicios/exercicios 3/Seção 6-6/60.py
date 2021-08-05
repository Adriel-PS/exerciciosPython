x=1
soma = 0
qnt,qutpar=0,0
media=0
maior=0
menor=10000000000000
mediapar=0


while x != 0 :
    x=int(input("informe os numeros"))

    if x==0 :
        break

    soma = soma + x
    qnt +=1
    media = (media+x)/qnt
    if x > maior :
        maior =x
    if x < menor :
        menor = x
    if x%2 == 0 :
        qutpar+=1
        mediapar = (mediapar+x)/qutpar
print(f"a soma é de {soma}, quantidade de numero digitados é de {qnt}, a media é de {media} , o maior numero é {maior} ,"
      f"o menor numero é {menor}, e a media dos pares é {mediapar}")
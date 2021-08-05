lista = []
impar = []

while len(lista) < 10:
    x = int(input("informe um numero de 0 a 50 "))
    if x > 50 or x < 0 :
        print("numero nao aceito ")
    else :
        lista.append(x)
print(f"lista {lista}")
backup = lista.copy()
while len(lista) > 0 :
    x = lista.pop()
    if x % 2 == 1 :
        impar.append(x)
impar.reverse()
print(f"impar{impar}")
impar.reverse()
backup.reverse()

while len(backup) > 0 :
    print(f"da lista : {backup.pop()}, {backup.pop()}")

while len(impar) > 0 :
    if len(impar) > 1 :
        print(f"do impar : {impar.pop()} , {impar.pop()}")
    else:
        print(f"do impar : {impar.pop()} ")





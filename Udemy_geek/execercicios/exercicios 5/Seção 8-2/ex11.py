def nota_aluno(n1,n2,n3,letra):
        if letra == "a":
            media = (n1+n2+n3)/3
            return f"a media é {media}"
        elif letra =="p":
            media= (n1*0.5)+(n2*0.3)+(n3*0.2)
            return f"a media é {media}"
        else:
            return "tipo informado nao é valido"

num1 = int(input("informe a primeira nota: "))
num2 = int(input("informe a segunda nota: "))
num3 = int(input("informe a terceira nota: "))

tipo = str(input("informe o tipo. A para media e P para peso:"))

print(nota_aluno(num1,num2,num3,tipo))

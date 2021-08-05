nota1=int(input("informe a nota do trabalho de laboratorio : "))
nota2=int(input("informe a nota da avaliação semestral : "))
nota3=int(input("informe a nota do exame final : "))
media = (nota1*0.2)+(nota2*0.3)+(nota3*0.5)
if media <= 2.9 :
    print(media,"aluno reprovado")
elif media >= 3 and media <= 4.9 :
    print(media,"aluno em recuperação")
else :
    print(media," aluno aprovado")
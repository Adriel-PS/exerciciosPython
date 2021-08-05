soma=0
sq=0
rq=0
fim=0
for num in range (1,101):
    multi = num * num
    soma = soma + multi
    sq = sq + num
    rq = sq *sq
fim = rq - soma
print(f"a soma dos quadrados é de {soma} ")
print(f"o resultado do quadrado da soma dos numeros de 1 a 100 é {rq}")
print(f"a diferença entre os numero é de {rq} - {soma} = {fim}")
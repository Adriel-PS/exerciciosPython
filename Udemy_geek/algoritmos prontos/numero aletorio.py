"""
obs : os numeros criando usando o metodo randint sao apenas natuais , e vao do primiero ao ultimo
escolhidos e incluiem o primeiro e ultimo

"""
import random
x= 0
while True:
    if x >= 10:
        break
    print(random.randint(0,10))
    x +=1
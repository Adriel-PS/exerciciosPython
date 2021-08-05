def quadrado(num):
    var = 1
    while var < num :
        if var * var == num:
            return f"é um quadrado perfeito"
        var = var+1
    else:
        return f"nao é um quadrado perfeito"
x=int(input("informe um numero: "))
print(quadrado(x))
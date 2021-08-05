for a in range (1,100):
    for b in range (1,100):
        for c in range(1, 100):
            soma = (a*a)+(b*b)
            if soma == c*c :
                print(f"os resultados sao {a}² + {b}² = {c}² = {soma}")
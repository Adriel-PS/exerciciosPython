i=1
x=(i+5*i)/(i+1)
vetor = []

while len(vetor) < 50 :
    vetor.append(x)
    i = len(vetor)
    x = (i + 5 * i) / (i + 1)
print(vetor)
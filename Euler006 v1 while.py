soma = 0
qsoma = 0
n = 1
while n <= 100:
    soma = soma + n*n
    qsoma += n
    n += 1
    print(soma,qsoma)
    
print(qsoma*qsoma-soma)
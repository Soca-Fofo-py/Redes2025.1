soma = 2 + 3
for n in range (4,2000000):
    ehprimo = True
    div = 2
    while div <= int(n**0.5) and (ehprimo==True):
        if n % div ==0:
            ehprimo = False
        div += 1
    if ehprimo ==0:
        soma += n
    if n % 10000 ==0:
        print(n)
print(soma)
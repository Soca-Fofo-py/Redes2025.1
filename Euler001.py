#https://projecteuler.net/problem=1
n = 1
soma = 0
while n < 1000:
    if n%3==0 or n%5==0:
        soma=soma+n
    #n = n + 1
    n += 1
	
print("A soma é",soma)
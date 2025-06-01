fat = int(input("Digite um numero: ")) 
produto = 1
n = 1
while n <= fat:
    produto = produto*n
    n = n + 1
print("O fatorial de",fat,"é",produto)
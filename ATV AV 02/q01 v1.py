num_1 = input("Digite um número: ") # temos uma string
num_2 = 0 # Um numero vazio

for x in num_1[::-1]:
    num_2 = int(x) + num_2*10
if int(num_1) == num_2:
    print(num_2,"é um palíndromo!")

'''
Faça um programa que recebe numero N e gera uma lista de 100 números aleatórios entre -N e +N (incluídos)
Filtre só os numeros pares desta lista
'''
import random
lista = []
N = int(input("Digite um número: "))

for x in range (100):
    new = random.randint(-N,N)
    lista.append(new)
print("A lista é:",lista)
print()
pares = list(filter(lambda x: x%2==0,lista))
print("Os pares são:",pares)
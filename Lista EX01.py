lista = []
num = int(input("Digite um número inteiro: "))
lista.append(num)
tamanho = 1
menor = num
maior = num

while num > 0:
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        lista.append(num)
        tamanho += 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
y = int(input("Qual número deseja procurar na lista? "))
vezesqueaparece = 0
for x in lista:
    if x == y:
        vezesqueaparece += 1
########################################## erro!
primeira_aparencia = -1
pos = 0
for z in lista:
    while pos <= tamanho:
        if z == y:
            primeira_aparencia == pos
        pos += 1
######################################### erro!
soma = 0
for w in lista:
    soma += w

print(lista,"de tamanho:",tamanho)
print("O maior é: ",maior)
print("O menor é: ",menor)
print("A soma de todos os elementos da lista é:",soma)
print("O número:",y,"aparece",vezesqueaparece,"vezes!")
print("A primeira aparência de:",y,"ocorre em:",primeira_aparencia)
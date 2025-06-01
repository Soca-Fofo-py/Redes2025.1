# A magia (ou pesadelo) dos juros compostos é que eles crescem que uma maneira
# inimaginável. Sabendo que o montante acumulado para um capital c, a uma taxa
# i (em porcentagem), por um tempo t é dado por:
# Montante = c . ( 1 + i / 100)^t
# Faça um programa que aceite os três parâmetros citados e informe o montante
# gerado pelo capital.
#
print("Este código calcula o montante gerado por um capital aplicado a juros compostos!")
c = int(input("Digite o valor do capital inicial: "))
i = int(input("Digite o valor da taxa (%) em um valor inteiro: "))
t = int(input("Digite o tempo em meses: "))
montante = (c*((1+i/100)**t))
print ("O montante total eh: ", montante)
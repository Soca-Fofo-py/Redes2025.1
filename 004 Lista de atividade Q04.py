# Usando os conceitos da questão 3 e sabendo que a taxa de juros (composto) do
# cartão de crédito é em torno de 12% ao mês, calcule o tempo em o valor de uma
# dívida de R$ 1000,00 se transforma em R$ 1.000.000,00
#   Lembre: loga c = logb c / logb a
#   Lembre: para usar log no python:
#import math
#print (math.log(2, 10)) # imprime o log decimal de 2
#
print("Este código calcula a quantidade necessária em meses para que uma dívida de 1.000,00 se torne 1.000.000,00!")
c = 1000
i = 12
t = 0
montante = 0
while montante<1000000:
    montante = (c*((1+i/100)**t))
    #print ("São necessários:",t-1,"meses para que a dívida chegue a R$:",montante)
    t = t+1
print ("São necessários:",t-1,"meses para que a dívida chegue a R$:",montante)
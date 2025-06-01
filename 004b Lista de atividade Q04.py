import math
print("Este código calcula a quantidade necessária em meses para que uma dívida de 1.000,00 se torne 1.000.000,00!")
montante = float(input("Digite o Montante: "))
c = int(input("Digite o valor do capital inicial: ")) #1000
i = int(input("Digite o valor da taxa (%) em um valor inteiro: ")) #12
t = math.log(montante/c)/math.log(1+i/100)
t = math.ceil(t)
#t = math.flor(t)
print ("O tempo para atingir o montante é",t,"meses")
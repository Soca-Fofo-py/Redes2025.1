# 02 Receba como entrada os coeficientes (inteiros) de uma equação de segundo grau: a, b e c, e apresente as raízes reais.
#
print("Este código calcula as raizes reais (X1 e X2) ao lhe serem apresentados os valores a, b e c de uma equação do segundo grau!")
a = int(input("Digite o valor 'a' em um valor inteiro: "))
b = int(input("Digite o valor 'b' em um valor inteiro: "))
c = int(input("Digite o valor 'a' em um valor inteiro: "))
delta = ((b**2)-4*a*c)
#print("O valor de delta eh: ",delta)
x1 = ((-b+delta**0.5)/(2*a))
print("O valor de X1 eh: ",x1)
x2 = ((-b-delta**0.5)/(2*a))
print("O valor de X2 eh: ",x2)
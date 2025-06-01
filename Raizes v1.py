print ("Este código ler os valores de a, b e c, e cálcula as raizes da equação de segundo grau associada!")

a = int(input("Digite o valor de (a):"))
b = int(input("Digite o valor de (b):"))
c = int(input("Digite o valor de (C):"))
delta = b**2-4*a*c
x1 = (-b+delta**0.5)/2*a
x2 = (-b-delta**0.5)/2*a
print("Os valores de x são respectivamente: X1=",x1,"e X2=",x2)
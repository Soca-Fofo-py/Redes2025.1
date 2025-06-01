print ("Este código ler os valores de a, b e c, e cálcula as raizes da equação de segundo grau associada!")

a = int(input("Digite o valor de (a):"))
if a !=0:
    b = int(input("Digite o valor de (b):"))
    c = int(input("Digite o valor de (C):"))
    delta = b**2-4*a*c

    if delta >= 0:
        x1 = (-b+delta**0.5)/2*a
        x2 = (-b-delta**0.5)/2*a
        if x1==x2:
            print("A unica raiz é:",x1)
        else:
            print("Os valores de x são respectivamente: X1=",x1,"e X2=",x2)
    else:
        print ("O valor de 'DELTA' é:",delta,"E por isso não existem raizes reais!")
else:
    print("Não é equação do 2° grau!!!")
    
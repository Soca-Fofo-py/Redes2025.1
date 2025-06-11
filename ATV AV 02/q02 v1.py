n = int(input("Digite um número: "))
m = int(input("Digite um segundo número: "))
fat = 1 #Valor innicial neutro de fat
for x in range(1,n+1):
    fat = fat*x
if fat%m==0:
    print(m,"é um Jaime de",n)
n = int(input("Digite um número ao qual deseja saber se é primo: "))
divisores = 0
for x in range(1,n//2+1):
    if n%x == 0:
        divisores +=1
        
print (divisores)
if divisores == 1:
    print(n,"é primo")
else:
    print(n,"não é primo!")
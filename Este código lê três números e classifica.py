#Este código lê três números INTEIROS e os classifica em ordem crescente!
#2025.Maio.02.sexta-feira
try:
    a=int(input("Digite um número: "))
    menor=a
    b=int(input("Digite novamente um número: "))
    if b<menor:
        menor=b
        medio=a
    else:
        medio=b
    c=int(input("Digite novamente um número: "))
    if c<menor:
        menor2=c
        medio2=menor
        maior2=medio
        print(menor2,medio2,maior2)
    else:
        if c<medio:
            menor3=menor
            medio3=c
            maior3=medio
            print(menor3,medio3,maior3)
        else:
            maior=c
            print(menor,medio,maior)
    print("FIM!")
except:
    print("Alguma coisa deu errado e a culpa foi sua!")
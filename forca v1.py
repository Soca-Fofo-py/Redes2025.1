import random
palavras = ("ABACATE","LIMA","ABACAXI","LIMAO")
segredo = palavras[random.randint(0,len(palavras)-1)]
visivel = "_"*len(segredo)
tentativas = 4 #(len(segredo))//2

while visivel != segredo and tentativas > 0 :
    print(visivel)
    letra = input("Digite uma letra: ")
    tentativas -= 1

#######################################################
    novavisual = ""
    for pos in range (len(segredo)):
        if letra == segredo[pos]:
            novavisual += segredo[pos]
        else:
            novavisual += visivel[pos]
    visivel = novavisual        
#######################################################
if visivel == segredo:
    print("Parabéns, você acertou!",segredo)
else:
    print("Esgotou-se suas tentativas!",segredo)
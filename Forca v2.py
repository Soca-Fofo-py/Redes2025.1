# 1,2,,4,,6 - Não cumpre os requisitos 3 e 5.

import random
palavras = ("ABACATE","LIMA","ABACAXI","LIMAO","PERA")
segredo = palavras[random.randint(0,len(palavras)-1)]
#[4]
segredo = segredo.upper()
visivel = "_"*len(segredo)
#[1]
tentativas = 4

while visivel != segredo and tentativas > 0 :
    print(visivel)
    letra = input("Digite uma letra: ")
    #[4]
    letra = letra.upper()
    tentativas = tentativas - 1

# Caixinha de comparação!
#######################################################
    novavisivel = ""
    for pos in range (len(segredo)):
        if letra == segredo[pos]:
            novavisivel += segredo[pos]
        else:
            novavisivel += visivel[pos]
            
    visivel = novavisivel
#######################################################

#[2] e [6]
if visivel == segredo:
    print("Parabéns, você acertou!, a palavra era:",segredo)
else:
    print("Esgotaram-se suas tentativas!, entretanto te ofereço a chance de ouro!")
    tent_ouro = input("Qual a palavra? ")
    tent_ouro = tent_ouro.upper()
    if tent_ouro == segredo:
        print("Parabéns, você acertou a chance de ouro, a palavra era:",segredo)
    else:
        print("Você não acertou a chance de ouro, a palavra era:",segredo)

print("FIM")

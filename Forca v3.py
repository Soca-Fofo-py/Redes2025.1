# 1,2,3,4,5,6
try:
    import random
    palavras = ("ABACATE","LIMA","ABACAXI","LIMAO","PERA","graviola","caja","caQUI","BaNaNa")
    segredo = palavras[random.randint(0,len(palavras)-1)]
    segredo = segredo.upper() #[4] [MAIÚSCULAS]
    visivel = "_"*len(segredo)
    tentativas = 4 #[1] [Limite de tentativas]

    while visivel != segredo and tentativas > 0 :
        print(visivel)
        letra = input("Digite uma letra: ")
        letra = letra.upper() #[4] [MAIÚSCULAS]

        # [3] e [5] [Não aceitar mais de uma letra nem letras repetidas]
        if len(letra) > 1 or visivel.count(letra) !=0 :
            print(letra,"Já foi digitado ou é mais que uma letra") # Opcional
            # Não altera 'segredo' nem 'tentativas'
        else:
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

    #[2] e [6] [Exibe sucesso e mostra segredo ou exibe falha e oferece chance de ouro]
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

    print("FIM") # Opcional
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!")

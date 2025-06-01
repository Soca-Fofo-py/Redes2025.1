# (2 pontos) Faça um programa que sorteia um número entre 1 e 100 (use a função
# randint) e faça até quatro perguntas ao usuário para que ele acerte o número.
# Em cada pergunta informe o intervalo de tentativa, que inicialmente é 1 a 100.
# Mas se o usuário indicar 35 e o número internamente sorteado for 72, a pergunta
# seguinte deve informar que o intervalo agora está de 36 a 100, e assim
# sucessivamente.
################################################################################


try:
    # Importa random!
    import random
    # Sorteia um número aleatorio de 1 a 100!
    rand_num = random.randint(1,100)
    #print(rand_num)                        ############################## para teste

    # Define tent, tentativas, intervalo_ini e intervalo_fin como variáveis. Sendo as três ultimas 
    # com válores iniciais do enunciado!
    tent = () # Essa será a variável para os valores a serem recebidos!
    intervalo_ini = 1
    intervalo_fin = 100
    print("Tente adivinhar o número entre o intervalo:",intervalo_ini,"e",intervalo_fin)
    # Recebe uma tentativa! Tentativa 01
    tent = int(input("Digite um numero: "))
    # Checa se acertou!
    if tent == rand_num:
        print("Parabéns, você acertou o numero!",rand_num)
    else:
        # Formação de novo intervalo!
        if rand_num > tent:
            intervalo_ini,intervalo_fin = tent+1,intervalo_fin
        else:
            intervalo_ini,intervalo_fin = intervalo_ini,tent-1
        #print(intervalo_ini,intervalo_fin) ############################## para teste

        print("Tente adivinhar o número entre o intervalo:",intervalo_ini,"e",intervalo_fin)
        # Recebe uma tentativa! Tentativa 02
        tent = int(input("Digite um numero: "))
        # Checa se acertou!
        if tent == rand_num:
            print("Parabéns, você acertou o numero!",rand_num)
        else:
            # Formação de novo intervalo!
            if rand_num > tent:
                intervalo_ini,intervalo_fin = tent+1,intervalo_fin
            else:
                intervalo_ini,intervalo_fin = intervalo_ini,tent-1
            #print(intervalo_ini,intervalo_fin) ############################## para teste

            print("Tente adivinhar o número entre o intervalo:",intervalo_ini,"e",intervalo_fin)
            # Recebe uma tentativa! Tentativa 03
            tent = int(input("Digite um numero: "))
            # Checa se acertou!
            if tent == rand_num:
                print("Parabéns, você acertou o numero!",rand_num)
            else:
                # Formação de novo intervalo!
                if rand_num > tent:
                    intervalo_ini,intervalo_fin = tent+1,intervalo_fin
                else:
                    intervalo_ini,intervalo_fin = intervalo_ini,tent-1
                    #print(intervalo_ini,intervalo_fin) ############################## para teste

                    print("Tente adivinhar o número entre o intervalo:",intervalo_ini,"e",intervalo_fin)
                    # Recebe uma tentativa! Tentativa 04
                    tent = int(input("Digite um numero: "))
                    # Checa se acertou!
                    if tent == rand_num:
                        print("Parabéns, você acertou o numero!",rand_num)
                    else:
                        print("Suas tentativas acabaram! O número era:",rand_num)
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa foi sua!")
#FIM
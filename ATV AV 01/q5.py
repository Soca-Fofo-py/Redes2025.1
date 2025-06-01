# (2 pontos) Em um estacionamento, as tarifas são as seguintes (cumulativas):
#   • Até duas horas: R$ 8,00/hora ou fração;
#   • Entre três e quatro horas: R$ 5,00/hora ou fração;
#   • Horas seguintes: R$ 3,00/hora ou fração.
#   • Depois de 12h, o custo passa a ser fixo: R$ 30,00 
# Faça um programa que leia o número de minutos que um veículo permaneceu no
# estacionamento e exiba o valor a ser pago pelo responsável. Como exemplo,
# considere que o carro ficou 310 minutos no estacionamento; o proprietário deve
# pagar: R$ 16,00 (pelas duas primeiras horas) + R$ 10,00 (pela terceira e quarta
# horas) + R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00
################################################################################


try:
    # Recebe o tempo estacionado em minutos!
    tempo_est = int(input("Digite em minutos o tempo que um veículo permaneceu estacionado: "))
    # Define a variável TotPag com o valor mínimo!
    TotPag = int(8)
    # Caso de menos de 60 minutos!
    if tempo_est<= 60:
        TotPag = 8
    # Arredondando(de forma ineficiente) e convertendo o tempo para horas!
    else:
        if tempo_est%60 >0:
            tempo_est = int(tempo_est/60)
            tempo_est = tempo_est + 1
        else:
            tempo_est = int(tempo_est/60)
    # Casos por intervalo de tempo!
    # Caso menos de 2 horas!
        if tempo_est > 1 and tempo_est <= 2:
            TotPag = tempo_est*8
    # Caso entre 2 e 4 horas!
        if tempo_est >2 and tempo_est <= 4:
            TotPag = (8*2) + ((tempo_est-2)*5)
    # Caso entre 4 e 12 horas!
        if tempo_est > 4 and tempo_est <= 12:
            TotPag = (8*2) + (2*5) +((tempo_est-4)*3)
    # caso mais que 12 horas!
        else:
            if tempo_est > 12:
                TotPag = 30
    # Exibe o valor final a ser pago!
    print("O valor a ser pago é R$:",TotPag)
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa foi sua!")
#FIM!
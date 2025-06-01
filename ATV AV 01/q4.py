# (2 pontos) Faça um programa que conte o número de dias decorridos entre duas
# datas dentro do mesmo ano, ou seja, o programa pergunta o dia inicial e o mês
# inicial e, depois, o dia final e o mês final. Considere que o ano não é bissexto.
# Faça verificações se a data informada é válida (exemplo, 31 de novembro de
# 2024, não é um dia válido).
################################################################################
try:
    # Lê dia e mês inicial!
    dia_ini = int(input("Digite o dia inicial: "))
    mes_ini = int(input("De qual mês: "))
    # Transformando a data inicial em dias julianos!
    if mes_ini == 1:
        dia_ju_ini = dia_ini
    if mes_ini == 2:
        dia_ju_ini = dia_ini + 31
    if mes_ini == 3:
        dia_ju_ini = dia_ini + 59
    if mes_ini == 4:
        dia_ju_ini = dia_ini + 90
    if mes_ini == 5:
        dia_ju_ini = dia_ini + 120
    if mes_ini == 6:
        dia_ju_ini = dia_ini + 151
    if mes_ini == 7:
        dia_ju_ini = dia_ini + 181
    if mes_ini == 8:
        dia_ju_ini = dia_ini + 212
    if mes_ini == 9:
        dia_ju_ini = dia_ini + 243
    if mes_ini == 10:
        dia_ju_ini = dia_ini + 273
    if mes_ini == 11:
        dia_ju_ini = dia_ini + 304
    if mes_ini == 12:
        dia_ju_ini = dia_ini + 334
    # Lê dia e mês final!
    dia_fin = int(input("Digite o dia final: "))
    mes_fin = int(input("De qual mês: "))
    # Transformando a data final em dias julianos!
    if mes_fin == 1:
        dia_ju_fin = dia_fin
    if mes_fin == 2:
        dia_ju_fin = dia_fin + 31
    if mes_fin == 3:
        dia_ju_fin = dia_fin + 59
    if mes_fin == 4:
        dia_ju_fin = dia_fin + 90
    if mes_fin == 5:
        dia_ju_fin = dia_fin + 120
    if mes_fin == 6:
        dia_ju_fin = dia_fin + 151
    if mes_fin == 7:
        dia_ju_fin = dia_fin + 181
    if mes_fin == 8:
        dia_ju_fin = dia_fin + 212
    if mes_fin == 9:
        dia_ju_fin = dia_fin + 243
    if mes_fin == 10:
        dia_ju_fin = dia_fin + 273
    if mes_fin == 11:
        dia_ju_fin = dia_fin + 304
    if mes_fin == 12:
        dia_ju_fin = dia_fin + 334
    # Exibe o esultado!
    else:
        print("Passaram-se",dia_ju_fin - dia_ju_ini,"dias, entre",dia_ini,"do",mes_ini,"até",dia_fin,"do",mes_fin)
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa foi sua!")
#FIM!
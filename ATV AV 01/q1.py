# 1) Faça um programa que recebe um número de até quatro algarismos
# (ou seja, deve ser menor do que 10000) e apresenta a soma dos algarismos.
################################################################################


# Quatro algarismos também aceitaria -9999, logo: (-10000 <var< 10000) and (var != 0)
# Assumir que deve ser me apresentado numeros inteiros!
try:
    # Recebe o numero a qual se deseja obter a soma dos seus algarismos!
    var_1 = int(input("Digite um número maior que '0' e menor que '10.000', para que seja apresentado a soma de seus algarismos: "))
    var_soma = 0
    # Checa se var_1 atende ou não aos requisitos!
    if var_1 >= 10000 or var_1 < 0:
        print ("Por favor, digite um número maior que '0' e menor que '10.000'!")
    else:
        # Definir os valores de cada posição!
        milhar = (var_1 // 1000) % 10
        centena = (var_1 // 100) % 10
        dezena = (var_1 // 10) % 10
        unidade = (var_1 % 10)
        # somar os valores em cada posição!
        var_soma = unidade + dezena + centena + milhar
    # Exibe o resultado!
    print("A soma dos algarismos de",var_1,"é:",var_soma)
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa foi sua!")
# FIM!
num = '1200'#(input("Digite um número de no máximo 4(QUATRO) algarismos, " \
            #"no qual ao menos dois deles são diferentes entre si e diferentes de 0, Exemplo: '0690': "))

# Verifica se valor inserido é válido a suas duas condições:
if len(num) == 4 and num.count("0") <= 2:
    print("valido")








else: print("Número inválido")
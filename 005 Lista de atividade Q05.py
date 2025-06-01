# Em tempos de reforma da previdência, é fundamental ser previdente. Uma
# estratégia é aplicar um capital inicial c e todo mês fazer um novo depósito d que
# em conjunto (capital inicial e depósitos) renderão a uma taxa de juros mensal i.
# Após n meses, o saldo da conta será dado por:
# Saldo = c . (1 + i/100)n + d . ((1 + i/100)n – (1 + i/100)) / (i/100)
# Faça um programa que calcule o saldo, dados os quatro parâmetros. Teste várias
# situações, por exemplo: para uma aplicação inicial de 1000 e aporte mensal de 500,
# com taxa de 2%, depois de quantos anos o investidor terá 100000?
#
print("Este códogo calcula o saldo resultante do conjunto de um capital inicial + depositos mensais aplicados a juros compostos!")
c = int(input("Digite o valor do capital inicial: "))
d = int(input("Digite o valor do deposito mensal: "))
i = int(input("Digite o valor da taxa (%) em um valor inteiro: "))
n = int(input("Digite o tempo em meses: "))
#saldo = (c * (1 + i/100)**n + d * ((1 + i/100)**n - (1 + i/100)) / (i/100))
x = (1+i/100)
saldo = (c * (x)**n + d * ((x)**n - (x)) / (i/100))
print("O saldo acumulado durante",n,"meses é: R$:",saldo)
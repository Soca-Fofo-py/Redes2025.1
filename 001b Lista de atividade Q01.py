print("Este código exibe o número mínimo de cédulas e moedas a serem retornadas como troco!")
ValorConta = int(input("Digite o valor total da conta: "))
ValorPago = int(input("Digite o valor pago pelo cliente: "))
troco = ValorPago-ValorConta
print("O troco eh: R$:",troco)

ced200 = troco//200
troco = troco%200
if ced200 != 0:
    print(ced200,"Cédula/s de R$:200")

ced100 = troco//100
troco = troco%100
if ced100 != 0:
    print(ced100,"Cédula/s de R$:100")

ced50 = troco//50
troco = troco%50
if ced50 != 0:
    print(ced50,"Cédula/s de R$:50")

ced20 = troco//20
troco = troco%20
if ced20 != 0:
    print(ced20,"Cédula/s de R$:20")

ced10 = troco//10
troco = troco%10
if ced10 != 0:
    print(ced10,"Cédula/s de R$:10")

ced5 = troco//5
troco = troco%5
if ced5 != 0:
    print(ced5,"Cédula/s de R$:5")

ced2 = troco//2
moeda = troco%2
if ced2 != 0:
    print(ced2,"Cédula/s de R$:2")
if moeda != 0:
    print(moeda,"Moedas de R$:1")
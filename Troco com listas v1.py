cedulas = [200,100,50,20,10,5,2]; ListaTroco = []; ValConta = 100; ValPago = 548; troco = ValPago-ValConta
'''
ValConta = int(input("Digite o valor da conta: "))
ValPago = int(input("Digite o valor pago: "))
troco = ValPago-ValConta
'''
for cedula in cedulas:
    if troco // cedula >= 1:
        ListaTroco.append([cedula , troco // cedula])
    troco = troco % cedula
for x in ListaTroco:
    print(f"{x[1]} Cédula(s) de {x[0]}")
if troco == 1:
    print ("E uma moeda de 1 Real.")
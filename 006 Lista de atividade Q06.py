# O ICMS pago pelo consumidor em um produto é em torno de 17%. As empresas
# recolhem esse valor ao longo da cadeia de produção/vendas. Assim, se uma
# empresa vende um produto por v, tendo comprado por c, ela só recolhe o imposto
# relativo à diferença. Faça um programa que aceita os valores de venda e compra
# de um produto e mostre o ICMS a ser recolhido pela empresa na operação.
#
print("Este código calcula o ICMS a ser recolhido pela empresa sobre uma venda!")
vendeu = float(input("Insira o valor da venda do produto em R$: "))
comprou = float(input("Insira o valor da compra do produto em R$: "))
ValorRecolhido = (vendeu-comprou)
#print (ValorRecolhido)
imc = (17*ValorRecolhido)/100
print("O valor a ser recolhido pela empresa eh: R$:",imc)
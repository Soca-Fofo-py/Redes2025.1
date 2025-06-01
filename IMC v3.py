print ("Calculo de IMC, classificação e grau de obesidade!")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em centimetros: "))
altura = altura/100
imc = peso/(altura**2)
imc = round(imc, 2)
#print (imc)
if imc <= 18.5:
    print("IMC: ",imc,"Magraza e Obesidade de grau 0.")
if 18.5 < imc < 24.9:
    print("IMC: ",imc,"Normal e Obesidade de grau 0.")
if 25.0 < imc < 29.9:
    print("IMC: ",imc,"Sobrepeso e Obesidade de grau I.")
if 30.0 < imc < 39.9:
    print("IMC: ",imc,"Obesidade e Obesidade de grau II.")
if imc >= 40.0:
    print("IMC: ",imc,"Obesidade Grave e Obesidade de grau III.")

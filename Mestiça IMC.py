# Código da mestiça
print ("Calculo de IMC!")

# Entrada de dados!
altura = (float (input ("digite sua altura em centimetros: ")))/100
peso = float (input ("digite seu peso em Kg: "))

# Cálculo de IMC!
imc = round(peso / (altura**2),2)
print ("Seu IMC é: ",imc)

# Classificação e grau de obesidade!
if imc <= 18.5:
   print ("Magreza.", "Grau de obesidade: 0")
elif 18.5 <= imc <= 24.9:
   print ("Normal.", "Grau de obesidade: 0")
elif 25 <= imc <= 29.9:
   print ("Sobrepeso.", "Grau de obesidade: 1")
elif 30 <= imc <= 39.9:
   print ("Obesidade.", "Grau de obesidade: 2")
elif imc >= 40:
   print ("Obesidade grave.", "Grau de obesidade: 3")

# Caso de sobrepeso!
if imc > 24.9:
    imc_a_perder = imc - 24.9
    Kg_a_perder = imc_a_perder*(altura**2)
    print("Quilogramas a perder para ficar dentro da classificação normal" , round(Kg_a_perder,2),"kg")

# Caso de magreza!

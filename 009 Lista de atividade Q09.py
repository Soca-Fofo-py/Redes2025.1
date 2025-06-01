# Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do
# veículo. Faça um programa que pergunta: o tempo da viagem (em minutos), o
# número de litros de combustível gasto (em l), o preço do litro de combustível
# (em R$) e a distância percorrida (em Km); após isso informa dados típicos de um
# computador de bordo: a velocidade média (Km/h), o custo da viagem com
# combustível (em R$), o desempenho do carro (em Km/l, l/h e R$/Km).
#
print("Este código detalha o desempenho de um veiculo durante uma viagem!")
tempo = float(input("Digite em minutos o tempo de viagem: "))
tempo = tempo/60 #Converte minutos em horas!
litros = float(input("Digite a quantidade de litros gastos no trajeto: "))
preco = float(input("Digite o valor do litro de combustível em R$: "))
distancia = float(input("Digite a distância percorrida em Km: "))
VelMed = distancia/tempo
CustoViag = distancia*preco
KporL = distancia/litros
LporH = litros/tempo
RsporT = (preco*litros)/distancia
print("A velocidade média durante a viagem foi de:",VelMed,"Km/h")
print("O custo total da viagem foi de R$:",CustoViag)
print("Com um desempenho de:",KporL,"Km/l,",LporH,"l/h e",RsporT,"R$/Km")
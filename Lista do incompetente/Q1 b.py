# Lendo a massa inicial!
Massa_inicial = float(input("Digite a massa inicial: "))
# Criando nova variável para guardar valor inicial!
Massa_em_decaimento = Massa_inicial
# Tempo inicial!
tempo_decorrido = 0

# Loop para decaimento de massa!
while Massa_em_decaimento > 0.5:
    Massa_em_decaimento /= 2
    tempo_decorrido += 50

# Separando o tempo decorrido em horas, minutos e segundos!
# Horas!
Horas_decorridas = tempo_decorrido // 3600
tempo_decorrido = tempo_decorrido % 3600
# Minutos!
Minutos_decorridos = tempo_decorrido // 60
tempo_decorrido = tempo_decorrido % 60
# Segundos!
Segundos_decorridos = tempo_decorrido

# Exibição de resultados seguindo modelo do enunciado!
print(f"Massa Inicial: {Massa_inicial} gramas")
print(f"Massa Final: {Massa_em_decaimento} gramas")
# {:02} ao final foramata para o valor ser exibido em duas casas!
print(f"Tempo de Decaimento: {Horas_decorridas:02}:{Minutos_decorridos:02}:{Segundos_decorridos:02}")
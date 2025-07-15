import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    #print(posicoes)
    botafogo = []
    #print(atletas)

    for atleta in atletas:
        if atleta["clube_id"] == 263: # Botafogo/RJ

            '''
            print (f"APELIDO: {atleta['apelido']}, NOME: {atleta['nome']}," +
                   f"POSIÇÃO: {atleta['posicao_id']}, PREÇO: {atleta['preco_num']}")
            '''

            nome_posicao = posicoes[str(atleta['posicao_id'])]["nome"]
            botafogo.append([ atleta['nome'] , atleta['apelido'] , nome_posicao , atleta['preco_num'] ])
    #print(botafogo)
    botafogo.sort (key=lambda x: x[3],reverse=True)
    #print(botafogo)
    for atleta in botafogo:
        print(f"{atleta[2]:10s} -> {atleta[1]:20s} -> {atleta[0]:50s} -> {atleta[3]:5.2f} ")

    '''
    botafogo = filter (lambda x: x['clube_id'] == 263, atletas)
    for atleta in botafogo:
        print (f"{atleta['apelido']} -> {atleta['nome']}")
    '''

except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")

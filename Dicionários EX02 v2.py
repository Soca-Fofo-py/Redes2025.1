import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    atletas = json.loads(dados)["atletas"]
    sort_list = []
    #print(atletas)

    for atleta in atletas:
        if atleta["clube_id"] == 263: # Botafogo/RJ
            '''
            print (f"APELIDO: {atleta['apelido']}, NOME: {atleta['nome']}," +
                   f"POSIÇÃO: {atleta['posicao_id']}, PREÇO: {atleta['preco_num']}")
            '''
            sort_list.append([ ("APELIDO:",atleta['apelido']) , ("NOME:", atleta['nome']) , ("POSIÇÃO:", atleta['posicao_id']) , ("PREÇO:", atleta['preco_num']) ])
    #print(sort_list[3][2])
    sort_list = sort_list.sort(key=[4])
    print(sort_list)
    '''
    botafogo = filter (lambda x: x['clube_id'] == 263, atletas)
    for atleta in botafogo:
        print (f"{atleta['apelido']} -> {atleta['nome']}")
    '''

except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")

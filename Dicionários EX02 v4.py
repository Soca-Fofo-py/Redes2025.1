import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    #print(posicoes.values())
    botafogo = []
    clubes = dados["clubes"]
    clube_id = 0
    var = "FLAMENGO"#input("Qual o nome do time: ").upper()
    for clube in clubes.values():
        if var == clube["nome_fantasia"].upper():
            clube_id = clube["id"]
            print(f"Time: {var}, com ID: {clube_id}")
            break
    poslist = []
    for x in posicoes.values():
        #print((x["nome"]))
        poslist.append(x["nome"])
    #print(poslist)

    if clube_id !=0:
        for atleta in atletas:
            if atleta["clube_id"] == clube_id:
                nome_posicao = posicoes[str(atleta['posicao_id'])]["nome"]
                botafogo.append([ atleta['nome'] , atleta['apelido'] , nome_posicao , atleta['preco_num'] ])
        botafogo.sort (key=lambda x: x[3],reverse=True)
        #print(botafogo)
        for atleta in botafogo:
            #print(atleta[2])
            if atleta[2] in poslist:
                print(f"{atleta[2]:10s} -> {atleta[1]:20s} -> {atleta[0]:50s} -> {atleta[3]:5.2f} ")
                bar = poslist.index(atleta[2])
                #print(bar)
                if bar > -1:
                    poslist.pop(bar)
        #print(poslist)

        '''
        for atleta in botafogo:
            print(f"{atleta[2]:10s} -> {atleta[1]:20s} -> {atleta[0]:50s} -> {atleta[3]:5.2f} ")
        '''
    
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")

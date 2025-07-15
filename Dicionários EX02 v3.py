import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    botafogo = []
    clubes = dados["clubes"]
    clube_id = 0
    var = input("Qual o nome do time: ").upper()
    for clube in clubes.values():
        if var == clube["nome_fantasia"].upper():
            clube_id = clube["id"]
            print(f"Time {var}, --> {clube_id}")
            break
    

    if clube_id !=0:
        for atleta in atletas:
            if atleta["clube_id"] == clube_id:
                nome_posicao = posicoes[str(atleta['posicao_id'])]["nome"]
                botafogo.append([ atleta['nome'] , atleta['apelido'] , nome_posicao , atleta['preco_num'] ])
        botafogo.sort (key=lambda x: x[3],reverse=True)
        for atleta in botafogo:
            print(f"{atleta[2]:10s} -> {atleta[1]:20s} -> {atleta[0]:50s} -> {atleta[3]:5.2f} ")
    
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")

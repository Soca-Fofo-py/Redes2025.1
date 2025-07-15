import requests, json # pip install requests
clubes = requests.get("https://api.cartolafc.globo.com/clubes").text
dClubes = json.loads(clubes)
#print(dClubes.values())
for clube in dClubes.values():
    if clube["nome"] == "BOT":
        print(f"ID do clube: {clube["id"]}, Nome do clube: {clube["nome_fantasia"]}" +
              f"e abreviação: {clube["abreviacao"]}")
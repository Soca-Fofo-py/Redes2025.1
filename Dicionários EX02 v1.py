import requests, json

clubes = requests.get("https://api.cartolafc.globo.com/clubes").txt
dClubes = json.loads(clubes)
for clube in dClubes.values():
    if clube["nome"] == "BOT":
        print(clube["id"], clube["nome_fantasia"])
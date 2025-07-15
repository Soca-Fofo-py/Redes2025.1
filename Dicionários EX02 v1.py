import requests, json # pip install requests
clubes = requests.get("https://api.cartolafc.globo.com/clubes").text
dClubes = json.loads(clubes)
for clube in dClubes.values():
    if clube["nome"] == "BOT":
        print(clube["id"], clube["nome_fantasia"])
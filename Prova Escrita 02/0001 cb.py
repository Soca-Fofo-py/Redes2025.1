import json
nomear = input("digite o nome do arquivo: ")
with open (f"{nomear}","r") as fdarq:
    for n in fdarq:
        dicio = (n)
    #dicio = json.loads("ata.txt")
print(dicio)
#json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
#json.loads('"\\"foo\\bar"') == '"foo\x08ar'
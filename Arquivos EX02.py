import json
fdLogs = open ('apache.logs', 'r')
ips = []
for log in fdLogs:
    ip = log.split()[0]
    ips.append(ip)
fdLogs.close()
#print(ips)

fdAquivo = open ('000 Testes.txt','w')
repetidos = []
for x in ips:
    if x not in repetidos:
        fdAquivo.write(x + "\n")
        repetidos.append(x)
fdAquivo.close()
#print(repetidos)



dicio= {}
for c in ips:
    dicio[c] = dicio.get(c,0) + 1
fdad = json.dumps(dicio)    
with open ("001 Testes" , "w") as fdArquivo2:
    fdArquivo2.write(fdad)
fdArquivo2.close()
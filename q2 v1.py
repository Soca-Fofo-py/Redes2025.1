fdLogs = open ("apache.logs", "r") ; Dici2 = {}

for log in fdLogs:
    data = log.split()[3]
    Dici2[data[data.find("[") + 1 : data.rfind(":")]] = Dici2.get( data[data.find("[") + 1 : data.rfind(":")] , 0 ) + 1
fdLogs.close

sortedDicio = sorted(Dici2.items(),key = lambda x : x[1] , reverse = True)
for dupla in sortedDicio:
    print(f"Nº de acessos: {str(dupla[1]):>4s}, Em: {dupla[0]}")
    break #Unica mudança.
# Sempre são 5 minutos
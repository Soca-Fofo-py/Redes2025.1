import matplotlib.pyplot as plt
fdLogs = open ("apache.logs", "r") ; Dici2 = {}

for log in fdLogs:
    data = log.split()[3]
    Dici2[data[data.find("[") + 1 : data.rfind(":")]] = Dici2.get( data[data.find("[") + 1 : data.rfind(":")] , 0 ) + 1
fdLogs.close

sortedDicio = sorted(Dici2.items(),key = lambda x : x[1] , reverse = True)
#
fd = open (r"resposta_data.txt" , "w") #write -> Escrita; Se não existir, cria. Se existir, apaga conteudo existente.
#
vardi = dict(sortedDicio)
plt.title ("Nº de acessos por data")
plt.ylabel ("# de erros")
plt.plot (Dici2.keys(), Dici2.values()) # Dici2 ou vardi
plt.show()
fdLogs.close()

#
for dupla in sortedDicio:
    print(f"Nº de acessos: {str(dupla[1]):>4s}, Em: {dupla[0]}")
    #
    fd.write (f"Nº de acessos: {str(dupla[1]):>4s}, Em: {dupla[0]}"+"\n")
    #fd.write (" ",end="\n")
    #fd.write ("opção de escrita\n")
    #
fd.close()
# Sempre são 5 minutos

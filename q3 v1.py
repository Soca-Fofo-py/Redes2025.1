fdLogs = open ("apache.logs", "r") ; Dici2 = {}
http_sc = {}
for log in fdLogs:
    data = log.split()[8]
    #print(data,end='--')
    http_sc[data] = http_sc.get(data, 0 ) + 1
#print(http_sc.values())

'''
total = 0
for n in http_sc.values():
    total += n
print (total)
'''
for i in http_sc.items():
    print(f"Código de erro: '{(i[0])}' ; Número de ocorrencias:{str(i[1]):>5s}")
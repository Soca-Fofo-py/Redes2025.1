fdLogs = open ("apache.logs", "r") ; Dici2 = {}

for log in fdLogs:
    data = log.split()[3]
    #print(data[data.find("[") + 1 : (data.find("["))+12])
    Dici2[data[data.find("[") + 1 : (data.find("["))+12]] = Dici2.get (data[data.find("[") + 1 : (data.find("["))+12] , {str(log.split())[0]:0})
    Dici2[data[data.find("[") + 1 : (data.find("["))+12]][log.split()[0]][0] += 1
    
    #break
fdLogs.close()
print(Dici2)
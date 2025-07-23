fdLogs = open ("apache.logs", "r")
Dici2 = {}

for log in fdLogs:
    #print("log",log)
    data = log.split()[3]
    
    #print("complex",data[data.find("[") + 1 : data.rfind(":")])
    busque = data[data.find("[") + 1 : data.rfind(":")]

    Dici2[busque] = Dici2.get( data[data.find("[") + 1 : data.rfind(":")] , 0 ) + 1

fdLogs.close
print(Dici2)
for x in Dici2:
    print(x,Dici2[x])

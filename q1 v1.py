fdLogs = open ("apache.logs", "r")
#var = []
var = set()
Dici2 = {}
for log in fdLogs:
    #print("log",log)
    data = log.split()[3]
    '''
    print(data.find("["))
    print(data.rfind(":"))
    print(data[1:18])
    '''
    #print("complex",data[data.find("[") + 1 : data.rfind(":")])
    busque = data[data.find("[") + 1 : data.rfind(":")]
    #print("busque",busque)
    Dici2[busque] = Dici2.get( busque , 0 ) + 1
"""
    #var.append(data)
    var.add(data)
    #print(len(var[0]),var)
    #print(type(var))
    find1 = (log.find("[")) +1
    find2 = (log.find("]")) -9
    #print(find1,find2)
    ######print(log[find1:find2]+"\n")
    #print(log[19:36]+"\n")
    break"""
fdLogs.close

'''dicioDatas = {}
for var2 in var:
    print("PRINT",var2[1:18],end="\n")
    temp = var2[1:18]
    print(temp,"temp")
    dicioDatas[var2] = dicioDatas.get( temp , 0 ) + 1
    print("Dicio Dentro",dicioDatas)
    break
print("Dicio Fora",dicioDatas)'''

print(Dici2)
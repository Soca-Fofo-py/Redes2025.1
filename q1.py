fdLogs = open ("apache.logs", "r")
var = set()
for log in fdLogs:
    ip = log.split()[3]
    var.add(ip)
    #print(var)
    find1 = (log.find("[")) +1
    find2 = (log.find("]")) -9
    #print(find1,find2)
    print(log[find1:find2]+"\n")
    #print(log[19:36]+"\n")
    #break
fdLogs.close

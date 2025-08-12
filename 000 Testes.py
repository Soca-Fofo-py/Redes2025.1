import json
fdLogs = open ('apache.logs', 'r')
ips = []
for n in fdLogs:
    print(n)
    break
for log in fdLogs:
    ip = log.split()[0]
    ips.append(ip)



fdLogs.close()
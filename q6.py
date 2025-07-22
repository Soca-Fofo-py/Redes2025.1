fdLogs = open ("apache.logs", "r")
ips = set()
for log in fdLogs:
    ip = log.split()[0]
    ips.add(ip)
fdLogs.close

fdIps = open ("ips.txt","w")
for ip in ips:
    fdIps.write(ip+"\n")
fdIps.close()

### OPICIONAL com with!
with open ("ipsWith.txt","w") as fdIpsWith:
    for ip in ips:
        fdIpsWith.write(ip+"    ")
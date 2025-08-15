import json
dicio = {'tomate':['cacas','asas'],'frura':['vacuo',585,6455]}

nomear = input("digite o nome do arquivo para salvar : ")
fdfile = open (f"{nomear}","w")
fdfile.write(json.dumps(dicio))
fdfile.close()
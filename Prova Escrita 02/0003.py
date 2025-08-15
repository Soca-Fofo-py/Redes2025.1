import json
dicio = {'tomate':['cacas','asas'],'frura':['vacuo',585]}
'''
#nomear = input("digite o nome do arquivo: ")
with open ("ava.txt","r") as fdarq:
    for x in fdarq:
        print(x)
    #dicio.dumps()
'''
dici2 = str(dicio)

fdfile = open ("aca.txt","w")
#dados = 'amalo'
#dados += 'seu'
#dados.dumps(dicio)
fdfile.write(dici2)
fdfile.close()

'''
nomear = input("digite o nome do arquivo: ")
with open (f"{nomear}","r") as fdarq:
    soma = 0
    for x in fdarq:
        #print(len(x))
        soma += len(x.split())
        #print(x.split())
    #dicio.dumps()
print(soma)
'''
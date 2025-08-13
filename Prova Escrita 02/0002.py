
try:
    nomear = input("digite o nome do arquivo: ")
    with open (f"{nomear}","r") as fdarq:
        soma = 0
        for x in fdarq:
            #print(len(x))
            soma += len(x.split())
            #print(x.split())
        #dicio.dumps()
    print(soma)
except: print("ERRO")

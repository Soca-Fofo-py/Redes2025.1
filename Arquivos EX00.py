# LER UM ARQUIIVO
fd = open ("doc1.txt" , "r") #read -> Leitura
dados = fd.read()
fd.close()

# ESCREVER PARA UM ARQUIVO
fd = open ("doc2.txt" , "w") #write -> Escrita; Se não existir, cria. Se existir, apaga conteudo existente.
fd.write ("Olá mundo!")
fd.close()

# ADICIONAR CONTEUDO A UM ARQUIVO
fd = open ("doc3.txt","a") #"append"; Escreve sem apagar conteudo existente.
fd.write ("Aló mundo!")
fd.close()

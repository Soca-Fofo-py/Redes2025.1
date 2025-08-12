
# ESCREVER PARA UM ARQUIVO
fd = open (r"dados2.txt" , "w",encoding='utf8') #write -> Escrita; Se não existir, cria. Se existir, apaga conteudo existente.
dados = "Este programa \n"
dados += "foi feito com python\n"
fd.write (dados)
fd.write ("Opção de escrita\n")
fd.write ("Opção de escrita 2")
fd.write ("\nOpção de escrita 3")
fd.close()
fdopen = open ("dados2.txt","r",encoding='utf8')
for linha in fdopen:
    print("--"+linha)
fdopen.close()
with open ("dados2.txt",'r',encoding='utf8') as texto:
    l = 1
    for i in texto:
        print(f"{i}{l}")
        l += 1
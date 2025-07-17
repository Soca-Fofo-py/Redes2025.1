
# ESCREVER PARA UM ARQUIVO
fd = open (r"dados2.txt" , "w") #write -> Escrita; Se não existir, cria. Se existir, apaga conteudo existente.
dados = "Este programa \n"
dados += "foi feito com python\n"
fd.write (dados)
fd.write ("opção de escrita\n")
fd.write ("opção de escrita 2")
fd.write ("\nopção de escrita 2")
fd.close()

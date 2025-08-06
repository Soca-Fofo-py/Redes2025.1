'''
1) (4 pontos) Faça um programa que permita o cadastramento de MAC adresses
vinculados a um CPF. O seu programa suportar as seguintes operações: 
a) cadastrar CPF; 
b) adicionar MAC address a um CPF; 
c) remover um MAC address de um CPF; 
d) remover o CPF (só permitir se não existirem MAC addresses vinculados);
e) listar os CPF cadastrados; 
f) listar os MAC adresses vinculados a um CPF; 
g) salvar o “banco de dados” em um arquivo (perguntar o nome do arquivo); 
h) ler o “banco de dados” de um arquivo (perguntar o nome do arquivo). 
Em todas as operações que requerem entrada de CPF e MAC adresses, valide-os.
'''
import json
import cpf # Importa uma função para validação de CPF!


tabela_cpf_mac = {12345678900:['00:1A:2B:3C:4D:5E','00:1B:2B:3A:4D:5C'] , 78945612300:['00:1C:2A:3B:4D:5E'] , 
                  74185296300:[], '11630408433':[]} #
#tabela_cpf_mac['11630408433'] = 145
#print(tabela_cpf_mac)

###################################################################################################################
# Função do menu principal!
def menu_principal():   
    print  (    "\n" + f"{'CÓDIGO':^6s} : AÇÃO QUE DESEJA REALIZAR\n" + 
                f"{'1':^6s} : Cadastrar CPF\n" + f"{'2':^6s} : Adicionar MAC address a um CPF\n" + 
                f"{'3':^6s} : Remover um MAC address de um CPF\n" + f"{'4':^6s} : Remover o CPF\n" + 
                f"{'5':^6s} : listar os CPF cadastrados\n" + 
                f"{'6':^6s} : listar os MAC adresses vinculados a um CPF\n" + 
                f"{'7':^6s} : Salvar o “banco de dados” em um arquivo\n" + 
                f"{'8':^6s} : ler o “banco de dados” de um arquivo\n" + 
                f"{'0':^6s} : Finaliza o programa\n\n" + "Digite o código da ação que deseja realizar: "
                )
    return int (input("Selecione sua opcao: "))
###################################################################################################################
###################################################################################################################
# Função de verificação de MAC Address!
# Um endereço MAC válido é composto por 12 dígitos hexadecimais (0-9 e A-F), 
# geralmente separados por dois pontos ou hífens, como 00:1A:2B:3C:4D:5E
def check_mac(mac : str) -> bool:
    if type(mac) != str:
        return False
    # Tenta converter para hexadecimal!
    var_2 = mac.split(':')
    for x in var_2:
        try:
            int(x , 16)
        except:
            return False
    # Checa se contem 12 caracteres!
    mac = mac.replace(":", "").replace("-", "")
    if len(mac) != 12:
        return False
    print("MAC Válido")
    return True
###################################################################################################################






# Chamado da função menu!
opcao = menu_principal()
###################################################################################################################
# Cadastra um CPF!
if opcao == 1:
    print("Cadastrar um CPF\n")
    var_1= input("Digite o CPF a qual deseja cadastrar: ")
    if cpf.cpf_valido(var_1) == True:
        # This method adds a key with a specified default value if the key is not already present in the dictionary.
        tabela_cpf_mac.setdefault(var_1,[])
    else:
        print("CPF Inválido!")
###################################################################################################################
###################################################################################################################
# Adicionar MAC address a um CPF!
if opcao == 2: 
    print("Adicionar MAC address a um CPF\n")
    var_3 = input("Digite a qual CPF deseja cadastrar um endereço MAC: ")
    if cpf.cpf_valido(var_3) == True:
        if var_3 in tabela_cpf_mac:
            var_4 = input("Digite o endereço MAC que deseja cadastrar: ")
            if check_mac(var_4) == True:
                lista_temp = tabela_cpf_mac[var_3]
                tabela_cpf_mac[var_3] = lista_temp.append(var_4)
                print(var_3,lista_temp,var_4,"test")
            else:
                print("O endereço MAC que deseja cadastrar é inválido!")
        else:
            print("O CPF informado não está cadastrado!")
    else:
        print("CPF Inválido!")
###################################################################################################################

elif opcao == 21:
    print("remover mac")
    #amigos_ate(10000)
elif opcao == 21:
    print("remover mac")
    #amigos_ate(10000)
else:
    print ("Opcao invalida.")

print(tabela_cpf_mac)






'''
comando = 9 # De 1 a 0, o 9 estava sobrando!
tabela_cpf_mac = {12345678900:['00:1A:2B:3C:4D:5E','00:1B:2B:3A:4D:5C'] , 78945612300:['00:1C:2A:3B:4D:5E'] , 
                  74185296300:[]}

while comando != 0:
    comando = int(input("\n" + f"{'CÓDIGO':^6s} : AÇÃO QUE DESEJA REALIZAR\n" + 
                    f"{'1':^6s} : Cadastrar CPF\n" + f"{'2':^6s} : Adicionar MAC address a um CPF\n" + 
                    f"{'3':^6s} : Remover um MAC address de um CPF\n" + f"{'4':^6s} : Remover o CPF\n" + 
                    f"{'5':^6s} : listar os CPF cadastrados\n" + 
                    f"{'6':^6s} : listar os MAC adresses vinculados a um CPF\n" + 
                    f"{'7':^6s} : Salvar o “banco de dados” em um arquivo\n" + 
                    f"{'8':^6s} : ler o “banco de dados” de um arquivo\n" + 
                    f"{'0':^6s} : Finaliza o programa\n\n" + "Digite o código da ação que deseja realizar: "
                    ))
    
    # Lista os CPF cadastrados!
    if comando == 5: # 5
        print("listando os CPF cadastrados!")
        for var in tabela_cpf_mac.keys():
            print("CPF:",var)

    # Lista os MAC adresses vinculados a um CPF!
    if comando == 6: # 6
        try:
            # Uso 11 dígitos e int() como verificação de CPF!
            CPF = int(input("Digite o CPF ao qual deseja cheacar os MACs a ele vinculado: "))
            if len(str(CPF)) == 11: 
                if CPF in tabela_cpf_mac.keys():
                    print(f"Listando os MAC adresses vinculados ao CPF: {CPF}")
                    print(tabela_cpf_mac.get(CPF,"Não há MACs vinculados a esse CPF"))
                else: print(f"Esse CPF '{CPF}' não está cadastrado!")
            else: print(f"O CPF: {CPF} é invalido!") # Diferente de 11
        except: print(f"O CPF informado é inválido!") # Diferente de inteiros


print("Código encerrado!")
'''
################################################
'''
import json
d = json.loads(texto) # Carrega banco de dados
t = json.dumps(d) #Converte dicionário em texto
'''
################################################





'''
tabela2 = {123654:[],987456:[]}
tabela = {2:"ok",45:55,"cpf":""}
print((tabela.items()))
tabela["cpf"]=(123456)
print((tabela.items()))
print((tabela2.items())) 
'''



'''
try:
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!")
'''
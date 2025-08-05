def cpf_valido (cpf): # (cpf:int)
    try:
        cpf = int (cpf)


    except: #ValueError:
        #raise Exception ("CPF Invalido.")
        return False
##############################################################
def cpf_valido ( cpf: str ) -> bool:
    if type (cpf) != str:
        return False
    
    if cpf.isdecimal() == False:
        return False
    
    if len(cpf) != 11:
        return False

    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * 10 - pos
    dv1 = 11 - soma % 11
    if dv1 >= 10:
        dv1 = 0

    cpf = cpf.replace(".","").replace("-","")
    try:
        
        cpf = int (cpf)


    except:
        return False
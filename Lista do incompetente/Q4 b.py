try:
    # Recebe número do usuário!
    num = input("Digite um número ao qual deseja verificar se o mesmo é um número de Armstrong: ")

    # Contando os digitos do número sem a função len()!
    digitos = 0
    for pos in num:
        digitos = digitos + 1

    # Somando todos os algarismos do número elevados a quantidade de digitos do número! 
    SomaDasPotencias = 0
    for var_1 in num:
        SomaDasPotencias = SomaDasPotencias + int(var_1)**int(digitos)

    # Checa se número inicial(num) é igual a número final(SomaDasPotencias) e exibe se é ou não um número  de Armstrong!
    if int(num) == SomaDasPotencias:
        print(f"{num} É um número de Armstrong, pois a soma de seus algarismos elevado a potência {digitos} " +
            f"é igual a {SomaDasPotencias}")
    else:
        print(f"{num} NÃO é um número de Armstrong, pois a soma de seus algarismos elevado a potência {digitos} " +
            f"é igual a {SomaDasPotencias}")
        
# try except para correção de erros!
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!, " +
          "tente digitar apenas números!")

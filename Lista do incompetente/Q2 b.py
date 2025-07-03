try:
    # Definição de alcance, isto é, de 0 a 1 Milhão, conforme enunciado!
    for num in range(0,1000000):
        # Filtra se multiplo de 2 ou 5!
        if num % 5 == 0 or num % 2 == 0:
            # Transformando número em string para trabalhar com o comando for!
            var_1 = str(num)
            # Atribuição de soma para uso no laço de for!
            soma = 0
            #
            for x in var_1:
                soma = soma + int(x)**5 # Alternar para int(x)**4 e checar com exemplo do enunciado!
            # Compara se número é igual a soma das potências de 5 de seus dígitos!
            if soma == num:
                # Exibe se a comparação anterior for verdadeira!
                print(num,soma)
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!")
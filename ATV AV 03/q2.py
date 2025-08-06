'''
2) (2 pontos) Faça um programa que conta quantos números palíndromos existem entre
10 e 100000. Um número é palíndromo quando tem o mesmo valor se lido da
esquerda para a direita ou da direita para a esquerda. Ex: 98189 é palíndromo. Não
use strings na sua resposta.
'''

try:
    # Criando função para retornar o reverso de um número!
    def reverso(n):
        reverso = 0
        while n > 0:
            reverso = reverso*10 + n%10
            n = n//10
        return reverso

    # Contador inicial de palindromos!
    contador = 0
    palindromos = [] # Opcional, NÃO PEDIDO NO ENUNCIADO!

    # Range a ser percorrido!
    for num in range (10,100000+1): # 100000

        # Comparação de número original com o seu reverso!
        if num == reverso(num):
            
            # Conta quantidade de palindromos!
            contador += 1
            palindromos.append(num) # Opcional, NÃO PEDIDO NO ENUNCIADO!

    print(f"Existem {contador} números palíndromos entre 10 e 100000")
    #print(palindromos) # Opcional, NÃO PEDIDO NO ENUNCIADO!
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!")
# 2025.maio.06.terça-feira
# ENUNCIADO: Seja X. , e Y. a posição inicial de um retângulo no plano cartesiano,
# o retângulo tem largura l e altura h. faça um programa que leia os dados de
# 2 retângulos e responda se eles tem interseção.
#
# Obtendo dados do primeiro retângulo!
# Obtendo largura l do primeiro retângulo!
try:
    Xi_retangulo_1 = int(input("Digite em INTEIROS o valor da posição inicial no eixo X do primeiro retângulo: "))
    Xf_retangulo_1 = (Xi_retangulo_1 + int(input("Digite o tamanho do segmento da reta no eixo X do primeiro retângulo: ")))
    # Obtendo altura h do primeiro retângulo!
    Yi_retangulo_1 = int(input("Digite em INTEIROS o valor da posição inicial no eixo Y do primeiro retângulo: "))
    Yf_retangulo_1 = (Yi_retangulo_1 + int(input("Digite o tamanho do segmento da reta no eixo Y do primeiro retângulo: ")))
    # Exibe os valores de Xi, Xf, Yi e Yf, apenas com proposito de melhorar a compreensão!
    print("Os valores de 'Xi, Xf, Yi e Yf' do primeiro retângulo, são respectivamente: ",Xi_retangulo_1,",",Xf_retangulo_1,",",Yi_retangulo_1,"e",Yf_retangulo_1)

    # Exatamente a mesma coisa, para os dados do segundo retângulo!
    Xi_retangulo_2 = int(input("Digite em INTEIROS o valor da posição inicial no eixo X do segundo retângulo: "))
    Xf_retangulo_2 = (Xi_retangulo_2 + int(input("Digite o tamanho do segmento da reta no eixo X do segundo retângulo: ")))
    Yi_retangulo_2 = int(input("Digite em INTEIROS o valor da posição inicial no eixo Y do segundo retângulo: "))
    Yf_retangulo_2 = (Yi_retangulo_2 + int(input("Digite o tamanho do segmento da reta no eixo Y do segundo retângulo: ")))
    print("Os valores de 'Xi, Xf, Yi e Yf' do segundo retângulo, são respectivamente: ",Xi_retangulo_2,",",Xf_retangulo_2,",",Yi_retangulo_2,"e",Yf_retangulo_2)

    # Checando se há interseção!
    if Xi_retangulo_2 > Xf_retangulo_1 or Xi_retangulo_1 > Xf_retangulo_2 or Yi_retangulo_2 > Yf_retangulo_1 or Yi_retangulo_1 > Yf_retangulo_2 :
        # Caso alguma das condições do 'if' seja verdadeira, exibe que não há interseção entre os retângulos!
        print("Não há interseção entre os retângulos informados!")

    # se todas as condições do 'if' falharem, o 'else' sera "executado", e conclui-se que há uma interseção entre os retângulos!
    else:
        # Exibe que há interseção entre os retângulos!
        print("Há uma interseção entre os retângulos informados!")
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa foi sua!")
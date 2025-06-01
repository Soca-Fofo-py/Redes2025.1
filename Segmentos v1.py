#Program que leia dois segmentos de reta no eixo x, especificados em termos das posições iniciais e finais. Determinar se há interseção.


ai = int(input("Digite ai: "))
af = int(input("Digite af: "))
bi = int(input("Digite bi: "))
bf = int(input("Digite bf: "))
if bi<af:
    print("Há interseção!")
else:
    if ai<bf:
        print("Há interseção!")
    else:
        print("Não há interseção!")
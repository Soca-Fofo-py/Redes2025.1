#Program que leia dois segmentos de reta no eixo x, especificados em termos das posições iniciais e finais. Determinar se há interseção.


ai = int(input("Digite ai: "))
af = int(input("Digite af: "))
bi = int(input("Digite bi: "))
bf = int(input("Digite bf: "))

if af<ai:
    af, ai = ai, af
if bf<bi:
    bf, bi = bi, bf


if bi>af:
    print("Não há interseção!")
else:
    if ai>bf:
        print("Não há interseção!")
    else:
        print("Há interseção!")
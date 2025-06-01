#Program que leia dois segmentos de reta no eixo x, especificados em termos das posições iniciais e finais. Determinar se há interseção.


ai = int(input("Digite ai: "))
af = (ai + int(input("Digite o tamnho de ai: ")))
bi = int(input("Digite bi: "))
bf = (bi + int(input("Digite o tamanho de bf: ")))
#print ("Valores de ai,af,bi,bf; respectivamente: ", ai,af,bi,bf)

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
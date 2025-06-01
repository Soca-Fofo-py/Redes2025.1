soma_quadrado=0
quadrado_soma=0
for x in range (1,101):
    soma_quadrado += x**2
    quadrado_soma += x
print ((quadrado_soma**2)-soma_quadrado)
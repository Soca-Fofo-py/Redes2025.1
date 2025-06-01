# (2 pontos) Faça um programa que receba a nota de aluno do IFRN nas duas
# primeiras unidades de uma disciplina e exiba a sua situação: “aprovado”,
# “reprovado” ou “em prova final”. Em caso de prova final, pergunte a nota na
# prova final e exiba a situação nessa nova circunstância: “aprovado” ou
# “reprovado”. As regras para os cálculos estão na página 59 da organização
# didática do IFRN
################################################################################


try:
    # Recebe as duas notas!
    nota_1 = int(input("Digite sua nota na primeira unidade de 0 a 100: "))
    nota_2 = int(input("Digite sua nota na segunda unidade de 0 a 100: "))
    # Calcula e exibe a media!
    media = (2*nota_1+3*nota_2)/5
    print ("Sua media é:",media)
    # Checa se reprovado ou aprovado!
    if media < 20:
        print ("Reprovado")
    if media >= 60:
        print ("Aprovado")
    # Caso de avaliação final!
    else:
        if media >=20 and media <60:
            # Recebe nota da avaliação final!
            ava_final = int(input("Digite a nota da sua avaliação final: "))
            # Chaca se aprovado por uma das três equações, exibindo "Aprovado" se assim for!
            if (media+ava_final)/2 >= 60 or (2*ava_final+3*nota_2)/5 >=60 or (2*nota_1+3*ava_final)/5 >= 60:
                print("Aprovado")
            else:
                # Caso não satisfaça uma das equações, exibe: "Reprovado"!
                print("Reprovado")
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa foi sua!")
#FIM!
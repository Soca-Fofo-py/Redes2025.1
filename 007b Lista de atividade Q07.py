# Em 2016.2, o aluno Galileu, do curso de Gestão Pública do IFRN, foi
# surpreendido com a seguinte pergunta dos colegas. Quanto eu preciso tirar na
# última prova de “Matemática Financeira” para passar por média?
# O professor da disciplina fez um trabalho e uma prova para cada uma das
# unidades. Para obter a nota de cada unidade, o trabalho tinha peso de 30% e a
# prova de 70%. Segundo os critérios do IFRN, a nota na disciplina é formada pela
# nota da primeira unidade (com peso 40%) e a nota da segunda unidade (com peso
# 60%); passa por média quem obtiver 6,0 ou mais.
# Dadas as notas: t1 (primeiro trabalho), p1 (primeira prova) e t2 (segundo
# trabalho), calcule a nota a obter na segunda prova para passar por média.
#
#mfn = (((((t1*3)+(p1*7))/10)*4)+((((t2*3)+(p2*7))/10)*6))/10
#
print("Este codigo calcula e exibe os pontos necessários na sua segunda avaliação, para que seja aprovado!")
t1 = float(input("Informe a nota do seu primeiro trabalho: "))
p1 = float(input("Informe a nota da sua primeira avaliação: "))
m1 = ((t1*3)+(p1*7))/10
print(m1,"Media da primeira unidade!")
t2 = float(input("Informe a nota do seu segundo trabalho: "))
p2 = 0
mtotal = 0
while mtotal <(6):
    m2 = ((t2*3)+(p2*7))/10
    mtotal = ((m1*4)+(m2*6))/10
    p2 = p2+0.5
    #print(m2,"M2 no while",mtotal,"MT no while")
    #print (p2,"Valor de p2 antes de +0.5")
#print(m2,"Media desejada na segunda unidade!")
print(p2-0.5,"pontos são necessários na segunda avaliação para ser aprovado!")
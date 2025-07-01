lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

import random
lstNotas = []
for n in range(len(lstNomes)):
    lstNotas.append([random.randint(0,100),random.randint(0,100),random.randint(0,100)])

#print(lstNotas) ################# Opicional


for pos in range (len(lstNomes)):
    #print(lstNomes[pos],lstNotas[pos], end="") #### end="" ########### Exibe para todos
    ######################################################
    if ((lstNotas[pos][0]*2) + (lstNotas[pos][1])*3) / 5 >= 60:
        print(lstNomes[pos],lstNotas[pos], end="") ########################### Exibe somente se aprovado
        print(" APROVADO",end="\n")
    #else:
        #print(" REPROVADO!!!",end="\n")
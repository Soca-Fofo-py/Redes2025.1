# Diviseivel por 4 e 400 e não por 100

ano = int(input("Ano? "))
	if ano % 400 == 0 or ano%4==0 and ano%100!=0:
	    print(ano,"é bissexto")
	else:
	    print(ano,"não é bissexto")

SalBrut = float(input("Digite seu salário bruto: "))
if SalBrut <= 2480.80:
    imposto = SalBrut - 0
    print("Pagando R$:",imposto,"de impostos, seu salário liquido é R$:", SalBrut - imposto)
else:
    if SalBrut <= 2826.65:
        imposto = (SalBrut*0.075) - 182.16
        print("Pagando R$:",imposto,"de impostos, seu salário liquido é R$:", SalBrut - imposto)
    else:
        if SalBrut <= 3751.05:
            imposto = (SalBrut*0.15) - 394.16
            print("Pagando R$:",imposto,"de impostos, seu salário liquido é R$:", SalBrut - imposto)
        else:
            if SalBrut <= 4664.68:
                imposto = (SalBrut*0.225) - 675.49
                print("Pagando R$:",imposto,"de impostos, seu salário liquido é R$:", SalBrut - imposto)
            else:
                imposto = (SalBrut*0.275) - 908.73
                print("Pagando R$:",imposto,"de impostos, seu salário liquido é R$:", SalBrut - imposto)

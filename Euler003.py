#num = 4224
num = int(input("Digite um número: "))
divisor = 2
maiordiv = -1
while num !=1:
    if num %divisor==0:
        num = num/divisor
        #print(num)
        if divisor > maiordiv:
            maiordiv = divisor
    else:
        divisor = divisor+1
        #print(divisor)
        if divisor > maiordiv:
            maiordiv = divisor

print("Maior divisor:",maiordiv)

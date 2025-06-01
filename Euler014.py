x = 1
while x < 1000:
    n = x
    ##########################
    print(n, end='->')
    while n > 1:
        if n %2==0:
            n = n//2
            #passos +=1
        else:
            n = n*3 + 1
            #passos +=1
        print(n, end='->')
    print()
    ##########################
    x = x + 1
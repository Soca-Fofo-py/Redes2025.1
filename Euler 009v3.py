for a in range(1,101): 
    for b in range(1,101):
        for c in range(1,101):
            if (a**2+b**2) == c**2 and c**2==25 and a<b<c:
                print(a,b,c)
                #break

print("Fim")
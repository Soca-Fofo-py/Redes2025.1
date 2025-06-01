for a in range(1,1001): 
    for b in range(1,1001):
        for c in range(1,1001):
            if (a**2+b**2) == c**2 and a+b+c==1000 and a<b<c:
                print(a,b,c)
                print("o produto de ",a,',',b,',','e',c,"é:",a*b*c)
                #break

print("Fim")

# 200 + 375 + 425 = 1.000
# 200 * 375 * 425 = 31.875.000
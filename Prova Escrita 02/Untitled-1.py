a = {'a':[1,5,6],'b':[9,6.4]}
for b in a.values():
    print(b)
    n = '6'
    for x in b:
        #print(x)
        if n in str(x):
            print(n)

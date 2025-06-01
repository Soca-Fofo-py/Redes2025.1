r1xi= int(input("r1xi"))
r1xf= int(input("r1xf"))
r1yi= int(input("r1yi"))
r1yf= int(input("r1yf"))

r2xi= int(input("r2xi"))
r2xf= int(input("r2xf"))
r2yi= int(input("r2yi"))
r2yf= int(input("r2yf"))

if (r2xf < r1xi) or (r2xi > r1xf):
    intersX = False
else:
    intersX = True
	
if (r2yf < r1yi) or (r2yi > r1yf):
    intersY = False
else:
    intersY = True
	
if intersX and intersY:
    print("Int. Retangulo")
	
else:
    print("Sem Int. Retangulo")
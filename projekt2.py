with open('nyilvántartás.txt','r', encoding='utf-8') as forrasfajl:
    nevek = forrasfajl.readline().strip().split(";")
    matek = forrasfajl.readline().strip().split(";")
    töri = forrasfajl.readline().strip().split(";")
    német = forrasfajl.readline().strip().split(";")
    magyar = forrasfajl.readline().strip().split(";")
össz_átlag = []
print("-----------------------------------------------------------------------------------------------------------------")

# matek átlag
összeg = 0
for i in matek:
    összeg = összeg + float(i)
átlag = összeg / 12
össz_átlag.append(átlag)
print("Az osztály matek átlaga: ", átlag)
min = matek[0]
max = matek[0]
for szam in matek:
  if szam < min:
    min = szam
  if szam > max:
    max = szam
print('A legrosszabb átlag az osztályban matekból: ', min)
print('A legjobb átlag az osztályban matekból: ', max)  
print("-----------------------------------------------------------------------------------------------------------------")

# töri átlag
összeg1 = 0
for a in töri:
    összeg1 = összeg1 + float(a)
átlag1 = összeg1 / 12
össz_átlag.append(átlag1)
print("Az osztály töri átlaga: ", átlag1)
min1 = töri[0]
max1 = töri[0]
for szam1 in töri:
  if szam1 < min1:
    min1 = szam1
  if szam1 > max1:
    max1 = szam1
print('A legrosszabb átlag az osztályban töriből: ', min1)
print('A legjobb átlag az osztályban töriből: ', max1)  
print("-----------------------------------------------------------------------------------------------------------------")
# német átlag
összeg2 = 0
for b in német:
    összeg2 = összeg2 + float(b)
átlag2 = összeg2 / 12
össz_átlag.append(átlag2)
print("Az osztály német átlaga: ", átlag2)
min2 = német[0]
max2 = német[0]
for szam2 in német:
  if szam2 < min2:
    min2 = szam2
  if szam2 > max2:
    max2 = szam2
print('A legrosszabb átlag az osztályban németből: ', min2)
print('A legjobb átlag az osztályban németből: ', max2)  
print("-----------------------------------------------------------------------------------------------------------------")

# magyar átlag
összeg3 = 0
for c in magyar:
    összeg3 = összeg3 + float(c)
átlag3 = összeg3 / 12
össz_átlag.append(átlag3)
print("Az osztály magyar átlaga: ", átlag3)
min3 = magyar[0]
max3 = magyar[0]
for szam3 in magyar:
  if szam3 < min3:
    min3 = szam3
  if szam3 > max3:
    max3 = szam3
print('A legrosszabb átlag az osztályban magyarból: ', min3)
print('A legjobb átlag az osztályban magyarból: ', max3)  
print("-----------------------------------------------------------------------------------------------------------------")
összes_átlag = 0
for q in össz_átlag:
   összes_átlag = összes_átlag + q

print("Az osztály összátlaga: ", összes_átlag / 4)


#Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane, exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. 
zn=int(input("introduceti ziua nasterii "))
ln=int(input("introduceti luna nasterii "))
an=int(input("introduceti anul nasterii "))
zc=int(input("introduceti ziua curenta "))
lc=int(input("introduceti luna curenta "))
ac=int(input("introduceti anul curent "))
virsta=(ac-an)
if(ac>an):
    if(lc<ln):
        print((virsta-1), "ani")
    elif(lc==ln) and (zc<zn):
        print((virsta-1), "ani")
    elif(lc==ln) and (zc>=zn):
        print((virsta), "ani")
    elif(lc>ln):
        print((virsta), "ani")
else:
    print("eroare")
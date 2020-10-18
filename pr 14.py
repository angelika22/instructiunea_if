#Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla? 
a=int(input("Ionel a sosit al "))
print("Ionel se va caza in casuta", end="")
if a%4==0:
    print(a//4)
else:
    print(a//4+1)
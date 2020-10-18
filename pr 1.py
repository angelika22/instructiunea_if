#Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj.
A=int(input("numarul curent pentru primul elev "))
a=int(input("punctajul pentru primul elev "))
B=int(input("numarul curent pentru al doilea elev "))
b=int(input("punctajul pentru al doilea elev "))
C=int(input("numarul curent pentru al treilea elev "))
c=int(input("punctajul pentru al treilea elev "))
if(b>a) and (b>c):
    print("Punctajul maxim il are elevul cu numarul curent", B)
if(c>b) and (c>a):
    print("Punctajul maxim il are elevul cu numarul curent", C)
if(a>b) and (a==c):
    print("Punctajul maxim il are elevul cu numarul curent", A)
if(a==b) and (a>c):
    print("Punctajul maxim il are elevul cu numarul curent", A)
if(a==b) and (a==c):
    print("Punctajul maxim il are elevul cu numarul curent", A)
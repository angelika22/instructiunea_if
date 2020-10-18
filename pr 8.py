#Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator.
a=int(input("primul numar e "))
b=int(input("al doilea numar e "))
if (a%2==0) and (b%2==0):
    if a>=b:
        print("a")
    else:
        print("b")
else:
    print("nu sunt numere pare")
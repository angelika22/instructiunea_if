#Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau IMPAR. 
a=int(input("primul numar "))
b=int(input("al doilea numar "))
c=int(input("al treilea numar "))
if a%2==0:
    print(a, "Par")
else:
    print(a, "Impar")
if b%2==0:
    print(b, "Par")
else:
    print(b, "Impar")
if c%2==0:
    print(c, "Par")
else:
    print(c, "Impar")
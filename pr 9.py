#Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor.
A=int(input("numarul de bile albe mari "))
a=int(input("numarul de bile albe mici "))
B=int(input("numarul de bile verzi mari "))
b=int(input("numarul de bile verzi mici "))
C=int(input("numarul de bile rosii mari "))
c=int(input("numarul de bile rosii mici "))
print("total sunt", A+a+B+b+C+c, "bile")
if (A+B+C) < (a+b+c):
    print("sunt mai multe bile mici", a+b+c)
elif (A+B+C) > (a+b+c):
    print("sunt mai multe bile mari", A+B+C)
else:
    print("numarul de bile mari mari egal cu numarul de bile mici", A+B+C)
if (A+a>=B+b) and (A+a>=C+c):
    print("cele mai multe bile sunt albe", A+a)
elif (B+b>=A+a) and (B+b>=C+c):
    print("cele mai multe bile sunt verzi", B+b)
else:
    print("cele mai multe bile sunt rosii", C+c)
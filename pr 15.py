#Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În ce clasa va fi repartizat (A, B, C, D sau E)?.
a=int(input("al citalea este Radu "))
if (a>0) and (a<=100):
    if (a>0) and (a<=20):
        print("A")
    if (a>20) and (a<=40):
        print("B")
    if (a>40) and (a<=60):
        print("C")
    if (a>60) and (a<=80):
        print("E")
    if (a>80) and (a<=100):
        print("D")

#La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi laturile unui triunghi. Ajutaţi-l pe Gigel să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici ca 32000, şi returnează DA sau NU. Observaţie: Trei numere pot fi laturile unui triunghi numai dacă fiecare este mai mic ca suma celorlalte două. 
a=int(input("primul numar dictat e "))
b=int(input("al doilea numar dictat e "))
c=int(input("al treilea numar dictat e "))
if(a<b+c) and (b<a+c) and (c<b+a):
    print("da")
else:
    print("nu")
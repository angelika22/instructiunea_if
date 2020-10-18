#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? 
a=100
x=int(input("pe ce loc sta Ionel "))
if x<=100:
    if (x>0) and (x<=40):
        print("Ionel a primit tricou alb")
    elif (x>40) and (x<=60):
        print("Ionel a primit tricou rosu")
    elif (x>60) and (x<=80):
        print("Ionel a primit tricou albastru")
    elif (x>80) and (x<=100):
        print("Ionel a primit tricou negru")
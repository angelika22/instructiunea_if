#Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele luate şi afişaţi notele pe care le va comunica părinţilor. 
a=int(input("prima nota este "))
b=int(input("a doua nota este "))
c=int(input("a treia nota este "))
if c>8:
    print("a,b,c")
if c<8:
    if a>c:
        print("a")
    if b>c:
        print("b")
    if a==b:
        print("a")
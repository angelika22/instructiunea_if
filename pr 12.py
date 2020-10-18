#“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă iubeşte
a=int(input("introduceti numarul "))
if a%5==1:
    print("... un pic")
elif a%5==2:
    print("mult")
elif a%5==3:
    print("cu pasiune")
elif a%5==4:
    print("la nebunie")
elif a%5==0:
    print("de loc")
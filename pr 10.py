#La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea numărul de boabe de porumb.
a=int(input("numarul de gaini "))
b=int(input("numarul de boabe de porumb "))
if (b//(a+1)) and (b%(a+1)==0):
    print("numarul de boabe este", (b/(a+1)), "egal")
elif b/a:
    print("curcanul copan a primit mai mult ", (b%(a+1)), "boabe")
#CONJUNCIÓN
from operator import indexOf


print("Conjuncion AND")

num1 = int(input('Escribe un numero mayor a 2 y menor a 5: '))

if num1 > 2 and num1 <5:
    print('El numero ', num1,' cumple con la condiciónl.\n')
else:
    print('El numero ',num1,' No se cumple con la condicion.\n')

#Disyuncion
print('COnjuncion Disyuncion (OR)')

palabra = input('Para cumplir con la condicion escribe "SI" o "YES": ')

if palabra == "si" or palabra == "yes":
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion no se ha cumplido.\n")

#NEGACION
print("NEgacion NOT")

num1 = int(input("Introduce un numero igual a 5: "))

if not num1 == 5:
    print("\nEl numero es diferente de cindo y si cumple la condicion.\n")
else:
    print("El numero es igual a cinco y no cumple la condicion.\n")
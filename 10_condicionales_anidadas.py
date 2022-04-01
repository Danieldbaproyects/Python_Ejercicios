from ast import In


print("===========")
print("CONVERTIDOR")
print("===========")

print("Menu de Opciones:\n")

print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero.\n")

num = int(input("Cual es tu opcion?: "))
num_pal =''

if num == 1:
    print("\nConvertidor de numero a palabra\n")
    num_pal = int(input("Cual es el numero que deseas convertir a palbra?: "))
    if num_pal == 1:
        print("El numero es 'UNO'")
    elif num_pal == 2:
        print("El numero es 'DOS'")
    elif num_pal == 3:
        print("El numero es 'TRES'")
    elif num_pal == 4:
        print("El numero es 'CUATRO'")
    else:
        print(f"El numero: {num_pal}, no esta registrado.\n FIN.")
elif num == 2:
    print("\nConvertidor de palabra a numero\n")
    num_pal = input("\nCual es el numero en letras que deseas converit a numero?: ")
    num_pal = num_pal.lower() #Esta funcion de lower sirve para convertir el contenido 
    # que hemoms registrado en en minusculas
    if num_pal == 'uno':
        print("El numero es '1'")
    #elif num_pal == 'Uno':
    #        print("El numero es '1'")
    elif num_pal == 'dos':
        print("El numero es: '2'")
    elif num_pal == 'tres':
        print("El numero es: '3'")
    elif num_pal == 'cuatro':
        print("El numero es: '4'")
    else:
        print(f"El valor {num_pal} no se encuentra registrado.\n FIN.")
else:
    print(f"Numero {num} no registrado en el menu de opcions.\n FIN.")
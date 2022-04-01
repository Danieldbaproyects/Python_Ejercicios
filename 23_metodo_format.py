nombre = "Daniel"
edad = 24
print("Hola {} tienes {} años.".format(nombre,edad))
#Metodo 2 
print("Hola {nombre1} tienes {edad1} años.".format(nombre1="Santiago",edad1=23))
#Metodo 3
print("Hola {0} tienes {1} años.".format(nombre,edad))
#Metodo 4
print(f"Hola {nombre} tienes {edad} años.")

# -------------------------------------------------------------
print(f"El resultado de lal suma de 5 + 23 es: {5+23}")

#Ejemplo 2
nombre = 'Andrea'
estatura = 1.8
edad = 34
print(f'Hola {nombre} tu estatura es {estatura} y tienes {edad} años.')

#Ejemplo 3
nombre = input("¿Cual es tu  nombre? : ")
num_uno = int(input("Introduce un numero: "))
num_do = int(input('Introduce un segundo numero: '))
print(f'Hola {nombre} el resultado de {num_uno} + {num_do} es: {num_uno + num_do}')
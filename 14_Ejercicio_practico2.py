#Numero Par y Impar
print("****************************************************")
print("*Programa que determin si un numero es par o impar *")
print("****************************************************")

num = int(input("Ingresa un numero entero: "))

if num % 2 == 0:
    print("El numero ", num, " es par.")
elif num % 2 == 1:
    print("El numero ", num," es impar.")

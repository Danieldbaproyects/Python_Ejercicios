#Numero mayo y menor
print("****************************************************")
print("*     Programa que determinar cual es mayor        *")
print("****************************************************\n")


num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa otro numero entero:"))
num3 = int(input("Ingresa nuevamente otro numero: "))
"""
if num1 > num2 and  num1 > num3:
    print(f"El numero {num1} es el mayor.")
elif num2 > num3 and num1 < num2:
    print(f"El numero {num2} es el mayor.")
elif num3 > num1 and num3 > num2: 
    print(f"El numero {num3} es el mayor.")
"""

if num1 > num2 and  num1 > num3:
    print(f"El numero {num1} es el mayor.")
else:
    if num2 > num3:
        print(f"El numero {num2} es el mayor.")
    else:
         print(f"El numero {num3} es el mayor.")
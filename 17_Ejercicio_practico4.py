#   CALCULADORA
print("Calculadora con una sola variable")

print("*********************")
print("* Menu de Opciones: *")
print("*********************")
print(" 1. Suma")
print(" 2. Resta")
print(" 3. Multiplicación")
print(" 4. División")
print(" 5. División entera")
print(" 6. Exponente")
print(" 7. Moodulo o resto\n")

num_opción = int(input("Introduce el numero de la opción: "))

if num_opción == 1:
    print("Elejiste Suma\n")
    num1 = int(input("Ingresa el primer numero: "))
    num1 += int(input("Ingresa el segundo numero: "))
    print(f"El resultado de la suma es: {num1}")
elif num_opción == 2:
    print("Elejiste Resta\n")
    num1 = int(input("Ingresa el primer numero: "))
    num1 -= int(input("Ingresa el segundo numero: "))
    print(f"El resultado de la resta es: {num1}")
elif num_opción == 3:
    print("Elejiste Multiplicacion\n")
    num1 = int(input("Ingresa el primer numero: "))
    num1 *= int(input("Ingresa el segundo numero: "))
    print(f"El resultado de la multiplicacion es: {num1}")
elif num_opción == 4:
    print("Elejiste División\n")
    num1 = float(input("Ingresa el primer numero: "))
    num1 /= float(input("Ingresa el segundo numero: "))
    print("El resultado de la division es: ", round(num1),2)
elif num_opción == 5:
    print("Elejiste División Entera\n")
    num1 = float(input("Ingresa el primer numero: "))
    num1 //= float(input("Ingresa el segundo numero: "))
    print(f"El resultado de la division entera es: {num1}") 
elif num_opción == 6:
    print("Elejiste Exponenciación\n")
    num1 = int(input("Ingresa el primer numero: "))
    num1 **= int(input("Ingresa el segundo numero: "))
    print(f"El resultado de la exponenciaciónn es: {num1}")
elif num_opción == 7:
    print("Elejiste Modulo o Resto\n")
    num1 = int(input("Ingresa el primer numero: "))
    num1 = int(input("Ingresa el segundo numero: "))
    print(f"El resultado del resto es: {num1}")
else:
    print(f'{num_opción} no se reconoce como instrucción.')


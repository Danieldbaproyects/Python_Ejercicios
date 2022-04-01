"""
sucesion de Fibonacci
EJERCICIO PRACTICO 5

Desarrollar un programa que imprima en pantalla la sucesion de 
Fibonacci desde el numero 0 hasta el numero 1207, de manera Horizontal.

Maximo de lineas 7
"""

num1, num2 = 0, 1
while num2 <= 1597:
    print(num1,num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2
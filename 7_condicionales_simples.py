print("Sistema para calcular el promedio de un alumno\n")
nombre = input("Ingresa tu nombre: ")
nota1 = float(input(f"{nombre} Ingresa tu nota de fisica: "))
nota2 = float(input(f"{nombre} ingresa tu nota de quimica: "))
nota3 = float(input(f"{nombre} ingresa tu nota de economia: "))

promedio = (nota1+nota2+nota3) / 3
promedio = int(promedio)
if promedio > 2.9:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ',promedio)

"""
        OTRA SOLUCION
if ((nota1 + nota2 + nota3) / 3) >= 3.0:
    print(f"{nombre} pasaste el semestre")
"""
print("fin")

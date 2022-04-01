print("Sistema para calcular el promedio de un estudiante\n")
nomb = input("Estudiante, ingrese su nombre: ")
not1 = float(input(nomb+" Ingrese su nota de matematicas: "))
not2 = float(input(nomb+" Ingrese su nota de Sociales: "))
not3 = float(input(nomb+" Ingrese su nota de investigacion: ")) 
"""
 promedio = (not1 + not2 + not3) / 3

if promedio <= 2.9:
    print(nomb," Reprobaste el semestre con: "+ str(round(promedio,2)))
else:
    print(f"{nomb} aprobaste el semestre con: ", round(promedio,2)) 
"""   

if (not1+not2+not3) / 3 >= 3.0:
    print(f"{nomb} aprobaste con una nota de: {(not1+not2+not3)/3}")
    print(f"{nomb} aprobaste con una nota de: {round((not1+not2+not3)/3),2}") 
else: 
    print(f"{nomb} reprobaste con una nota de: " + str((not1+not2+not3)/3))
    print(f"{nomb} reprobaste con una nota de: " + str(round((not1+not2+not3)/3 ,2)))

print("fin operacion.")

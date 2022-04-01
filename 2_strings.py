mensaje = 'Hola'
mensaje += " "
mensaje += 'Daniel'
print(mensaje)

# CONCATENACION
mensaje1 = "Hola"
espacio = " "
nombre = "Daniel"
print(f"{mensaje}"+espacio+nombre)

num1 = 4
num2 = 6
resul = num1 + num2 
print("El resultado de la suma es: "+ str(resul))

# LA BUSQUEDA
print("\n###### BUSQUEDA por POSICION #####")
mensaje2 = "Hola Daniel"
buscar_subcadena = mensaje2.find("Daniel")
print(buscar_subcadena)

# LA EXTRACCION
print("\n### LA EXTRACCION por POSICIÓN ###")
mensaje3 = "Hola Daniel"
extraer_cadena = mensaje3[1:8] #Aqui vamos a extraer lo que esta contenido en la posicion 1 al 8
print(extraer_cadena)

# COMPARACION
print("### COMPARACION ###")
mensaje_uno = "Hola"
mensaje_dos = "Hol"
print(mensaje_uno == mensaje_dos)
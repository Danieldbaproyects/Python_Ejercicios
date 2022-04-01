# EJEMPLO para BREAK
print("WHILE con la sentencia BREAK\n")
contador = 0
while contador <= 10:
    contador += 1

    if contador == 5:
        break
    print("Valor acutal de la variable: ", contador)

print("Fin del programa, la sentencia se ha ejecutado.")

# EJEMPLO PARA  CONTINUE
print("\nWHILE con la sentencia Continue\n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue
    print("Valor acutal de la variable: ", contador)

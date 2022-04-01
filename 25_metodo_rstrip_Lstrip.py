'''
# RSTRIP()
- El metodo rstrip(), se utiliza para eliminar unicamente caracteres especificados
al final de una cadena.
- Al igual  que el medoto strip(), si no se especifica uno o mas caracteres
a eliminar, solo eliminara espacios en blanco y saltos en linea.
'''
candena = '\tHola Daniel\n'
print(candena)

candena = candena.rstrip("s ile\t\n")
print(candena)
'''
# LSTRIP()
- El metodo lstrip(), se utiliza para eliminar unicamente caracteres especificados
al inicio de una cadena.
- Al igual que los metodos anteriores, si no se especifica uno o mas caracteres a 
eliminar, solo eliminara espacios en blanco y saltos de linea.
'''
candena = '\tHola Danieliito\n'
print(candena)

candena = candena.lstrip("Ho la\t\n")
print(candena)

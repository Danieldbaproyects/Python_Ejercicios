'''
En python al trabar con cadenas de caracteres, en ocaciones surge la necesidad de eliminar espacios
en blanco o algun caracter en especifico, ya sea al inicio o bien al final de la cadena,

Para apoyarnos ante esta situación, en python contamos con tres metodos de gran utilidad.

strip(), lstrip() y, rstrip()

El metodo strip(), se utiliza para eliminar caracteres especificados al inicio y al final de una cadena
de caracteres, tomando en cuenta que si a el metodo strip() no se le especifica uno o mas caracteres
a eliminar, solo eliminara espacios en blanco y saltos en linea.
'''
cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.strip('s tHo\t\n')
print(cadena)

cadena1 = '\tHola Daniel\n'
print(cadena1)

cadena1 = cadena1.strip("i leHo\t\n")
print(cadena1)
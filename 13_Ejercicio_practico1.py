# SISTEMA CONTROL VACIONAL 
print("**************************************")
print("* Sistema de control vaccional Rappi *")
print("**************************************\n")

name_employeer = input("Empleado\nIngresa tu nombre: ")
key_departament = int(input("Ingresa la clave de tu departamento: "))

if key_departament == 1 or key_departament == 2 or key_departament == 3:
    
    yearsworks = float(input("Cuantos años llevas trabajando?: "))
    
    if key_departament == 1:
        if yearsworks >= 1 and yearsworks <2 :
            print(f"\n{name_employeer} tienes 6 dias de vacaciones.\nFIN.")
        elif yearsworks >= 2 and yearsworks <=6:
            print(f"{name_employeer} tienes 14 dias de vaciones.\nFIN.")
        elif yearsworks >= 7:
            print(f"{name_employeer} tienes 20 dias de vacaciones.\nFIN.")
        else: 
            print(f"{name_employeer}Sin derecho a vacaciones.\nFIN.")
    elif key_departament == 2:
        if yearsworks >0 and yearsworks < 2:
            print(f"{name_employeer} tienes 7 dias de vacaciones.\nFIN.")
        elif yearsworks >= 2 and (not yearsworks >= 7):
            print(f"{name_employeer} tienes derechoa 15 dias de vacaciones.\nFIN.")
        elif not yearsworks <=6:
            print(f"{name_employeer} tienes 22 dias de vacaciones.\nFIN.") 
        else:
            print(f"{name_employeer}Sin derecho a vacaciones.\nFIN.")
    elif key_departament == 3:
        if  yearsworks > 0 and yearsworks < 2:
            print(f"{name_employeer} tienes 10 dias de vacaciones.\nFIN.")
        elif yearsworks >= 2 and yearsworks <= 6:
            print(f"{name_employeer} tienes 20 dias de vacaciones.\n FIN.")
        elif yearsworks > 6:
            print(f"{name_employeer} tienes 30 dias de vacaciones.\nFIN.")
        else:
            print(f"{name_employeer}Sin derecho a vacaciones.\nFIN.")

else:
    print(f"La clave: {key_departament} no existe.\nFIN")
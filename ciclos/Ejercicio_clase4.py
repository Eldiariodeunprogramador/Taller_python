# MENÙ INTERACTIVO, CICLO WHILE: MUESTRA EN LA CONSOLA UN MENÙ CON LAS 
# OPCIONES 1) MENSAJE DE BIENVENIDA. 2) FECHA Y HORA ACTUAL. 3) SALIR 
# DEL PROGRAMA....

while True:
    print("\n ================ MENÙ ============================")
    print("(1) SUMAR ===========================")
    print("(2) RESTAR =============================")
    print("(3) SALIR DEL PROGRAMA ==============================")

    opcion = input("SELECCIONE UNA OPCION: ")

    if opcion == "1":
        print("SUMAR")
    elif opcion == "2":
        # CALCULO MANUAL DE FECHA/HORA SIN LIBRERIAS COMPLEJAS              
        print(f"Restar")
    elif opcion == "3":
        print("Saliendo del programa, ¡Hasta pronto!")
        break
    else:
        print("Opciòn no vàlida, intente nuevamente")
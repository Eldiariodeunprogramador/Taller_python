# MENÙ INTERACTIVO, CICLO WHILE: MUESTRA EN LA CONSOLA UN MENÙ CON LAS 
# OPCIONES 1) MENSAJE DE BIENVENIDA. 2) FECHA Y HORA ACTUAL. 3) SALIR 
# DEL PROGRAMA....

while True:
    print("\n ================ MENÙ ============================")
    print("(1) MENSAJE DE BIENVENIDA ===========================")
    print("(2) FECHA Y HORA ACTUAL =============================")
    print("(3) SALIR DEL PROGRAMA ==============================")

    opcion = input("SELECCIONE UNA OPCION: ")

    if opcion == "1":
        print("Bienvenido al programa! Espero que disfrute de la experiencia")
    elif opcion == "2":
        # CALCULO MANUAL DE FECHA/HORA SIN LIBRERIAS COMPLEJAS
        from datetime import datetime
        ahora = datetime.now()
        print(f"la fecha y hora actua:  {ahora}")
    elif opcion == "3":
        print("Saliendo del programa, ¡Hasta pronto!")
        break
    else:
        print("Opciòn no vàlida, intente nuevamente")
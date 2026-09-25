# TRY / EXCEPT BLOQUE QUE INTENTA EJECUTAR CÓDIGO Y CAPTURA EL ERROR SI OCURRE. ================================================
# VALUE ERROR EXCEPCIÓN CUANDO EL VALOR TIENE EL TIPO CORRECTO PERO UN CONTENIDO INVALIDO ======================================
# ELSE / FINALLY ELSE EJECUTA SI NO HUBO ERROR; FINALLY EJECUTA SIEMPRE... =====================================================
# RAISE: LANZA UNA EXCEPCIÓN MANUALMENTE CUANDO LOS DATOS NO CUMPLEN UNA REGLA... ==============================================
# EJERCICIO 1: TRY / EXCEPT BÁSICO =============================================================================================
# SIN MANEJO DE ERRORES, INGRESAR, "HOLA" EN LUGAR DE UN NÚMERO... PROVOCARIA UN ValueError Y EL PROGRAMA SE DETENDRÍA =========
# BOTÓN WINDOWS + PUNTO ME PERMITE AGREGAR UN EMOTICO

try: 
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es {numero}")
except ValueError:
    print(f"Error, debe ingresar un número entero válido ✖️")
    
# SI ESCRIBO LA PALABRA HOLA COMO NÚMERO MOSTRARÁ UN ERROR, QUE INDICA QUE EL NÚMERO INGRESADO ES INCORRECTO E INGRESAR UN ENTERO
# VÁLIDO, PERO SI SE INGRESA UN NÚMERO ENTERO VÁLIDO MOSTRARÁ EL MENSAJE EL NÚMERO INGRESADO, Y EL VALOR DEL NÚMERO INGRESADO  
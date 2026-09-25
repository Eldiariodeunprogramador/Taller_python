# EJERCICIO 1: TRY / EXCEPT BASICO ==============================
# SIN MANEJO DE ERRORES, INGRESAR HOLA, EN LUGAR DE UN NÙMERO ===
# PROVOCARÌA UN ValueError Y EL PROGRAMA SE DETENDRÌA ===========

try: 
    numero = int (input("Ingrese un nùmero entero: "))
    print(f"El nùmero ingresado es {numero}")
except ValueError:
    print("Error: debe ingresar un nùmero entero vàlido ")


# LA SALIDA DE ESTE CÒDIGO ES: ERROR, DEBE INGRESAR UN NÙMERO ENTERO
# VÀLIDO ... =======================================================    

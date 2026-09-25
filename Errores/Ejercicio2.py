# ========== EJERCICIO 2: DIVISIÒN SEGURA CON ZeroDivisionError.....
# ========== CAPTURAR EL ERROR DE DIVISIÒN ENTRE CERO (ZeroDivionError)
# ========== AL REALIZAR UNA OPERACIÒN ARITMÈTICA ...=================

try:
    dividiendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividiendo / divisor
    print(f"Resultado: {dividiendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese ùnicamente valores numèricos.")

# ========== ERROR: NO ES POSIBLE DIVIDIR ENTRE CERO... ============
# ========== AL INGRESAR LOS VALORES 10, 0 SE MOSTRARÀ EL MENSAJE ==
# ==================================================================    
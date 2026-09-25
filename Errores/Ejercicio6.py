# ===================================================================
# ========== EJERCICIO 6: CALCULADORA CON MANEJO DE ERRORES =========
# ===================================================================
# ===================================================================

try: 
    num1 = float(input("Ingrese el primer nùmero: "))
    num2 = float(input("Ingrese el segundo nùmero: "))
    operador = input("Ingrese el operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador =="*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        resultado = num1 / num2
    else:
        print("El operador no es vàlido")
        exit()

    print(f"Resultado: {resultado}")


except ValueError:
    print("Error: debe ingresar valores numèricos vàlidos")

except ZeroDivisionError as e:
    print(f"Error: {e}")

# ==================================================================
# =========== ENTRADA: 2, 4, * SALIDA: 8.0 =========================
# =========== ENTRADA: 2, 4, + SALIDA: 6 ===========================
# =========== ENTRADA: TRES SALIDA: ERROR, DEBE INGRESAR VALORES ===
# =========== NUMERICOS VÀLIDOS ====================================#    
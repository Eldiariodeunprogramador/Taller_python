# ==================================================================
# ==================================================================
# ========== EJERCICIO 3: ELSE Y FINALLY ===========================
# ========== USAR EL BLOQUE ELSE (SE EJECUTARA SI NO HUBO ERROR), ==
# ========== FINALLY (SE EJECUTA SIEMPRE, HAYA O NO ERROR)==========
# ========== ELSE - SE EJECUTA SOLO SI NO OCURRIO NINGUA EXCEPCIÒN =
# ========== =======================================================

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un nùmero entero.")
else:
    if edad >= 18:
        print("Acceso permitido")
    else:
        print("Acceso denegado: debe ser mayor de edad")

finally:
    print("Verificaciòn finalizada.")

# ==================================================================
# ========== AL INGRESAR LA ENTRADA VEINTE OBTENDRÀ LA SALIDA ======
# ========== ERROR: LA EDAD DEBE SER UN NÙMERO ENTERO, VERIFICACIÒN
# ========== FINALIZADA ... SI INGRESA UN NUMER POR EJEMPLO 20 SE ==
# ========== EJECUTARA EL MENSAJE: ACCESO PERMITIDO ================    

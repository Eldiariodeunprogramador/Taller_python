#====================================================================
# =========== EJERCICIO 8: VALIDAR FECHA DD/MM/AAAA =================
# ===================================================================
# ===================================================================

fecha = input("Ingrese la fecha en formato DD/MM/AAAA")

try:
    dia, mes, anio = map (int, fecha.split('/'))

    if not (1 <= dia <=31):
        raise ValueError("El dia debe estar entre 1 y 31")
    if not (1 <= mes <=12):
        raise ValueError("El mes debe estar entre 1 y 12")
    if anio <= 0:
      raise ValueError("El año debe ser positivo")

    print(f"fecha valida {dia:02d}/{mes:02d}/{anio}")    

except ValueError as e:
    print(f"Fecha invalida: {e}")

# ====================================================================
# ========= ENTRADA: 02/02/1984 .... SALIDA: 02/02/1984 ==============
# ====================================================================
# ====================================================================
# ===== SI SE INGRESA POR EJEMPLO UN TEXTO EL RESULTADO SERÀ =========
# ===== FECHA INVALIDA: INVALID LITERAL FOR INT() WITH BASE 10: "HOLA"
# ====================================================================#    
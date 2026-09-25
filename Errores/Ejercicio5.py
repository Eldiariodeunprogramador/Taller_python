# ====================================================================
# =========== EJERCICIO 5: RAISE, LANZAR ERRORES PERSONALIZADAS ======
# =========== USAR RAISE PARA GENERAR UNA EXCEPCIÒN MANUALMENTE CUANDO
# =========== LOS DATOS NO CUMPLEN UNA CONDICION DE NEGOCI ===========
# ====================================================================

def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacìa.")
    return sum(notas) / len(notas)

try:
    n = int(float(input("¿Cuàntas notas vas a ingresar?")))
    notas = []
    for i in range(n):
        notas = float(input(f" Nota {i + 1}: "))
        notas.append(notas)
    promedio = calcular_promedio(notas) 
    print(f"Promedio: {round(promedio, 2)}")   
except ValueError as e:
    print(f"Error: {e}")    

# ===================================================================
# ============ ENTRADA: 0 | SALIDA: ERROR: LA LISTA DE NOTAS NO PUEDE
# ============ ESTAR VACÌA ==========================================
# ===================================================================
# =================================================================== 
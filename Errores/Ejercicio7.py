# ===================================================================
# ============= EJERCICIO 7: ABRIR ARCHIVO CON MANEJO DE AUSENCIA ===
# ===================================================================
# ============= LEER ARCHIVO ========================================

nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo: ")
        print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo {nombre_archivo} no fue encontrado.")

# ==================================================================
# ==================================================================
# ==================================================================#
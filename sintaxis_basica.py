# ====================================================================
# ==================== INTRODUCCIÒN A LAS VARIABLES CON PYTHON =======
# ====================================================================
# Una variable permite almacenar un dato para luego utilizarlo.
# posteriormente dentro del programa. 
# Vamos a comenzar declarando cuatro variables.

nombre = "Leonel Ospina Restrepo" 
# Esta es una variable de tipo string. 
documento = 987072554
# Esta es una variable de tipo int (nùmero entero).
direccion = "Calle 106 D # 82 A 42, Medellìn"
tiene_deudas = True

# ==================================================================
# ============ MOSTRAR EL CONTENIDO DE UNA VARIABLE ================

print(nombre)

# ==================================================================
# =================== CONCATENACIÒN USANDO + =======================

print("CONCATENACIÒN USANDO +")
print("=" * 30)

# ==================================================================
# El operador + permite unir textos. Cuando usamos el operador +, 
# todos los elementos deben ser strings. 
# Si la variable es un intero (int), por lo que esta lìnea producirà un error. 
# print("Mi nombre es: " + nombre + "y mi documento es: " + documento), para
# solucionar este inconveniente podemos convertir el nùmero a texto utilizando str().

print("Mi nombre es: " + nombre + " y mi documento es: "+ str(documento))

# ======================================================================================
# ============= CONCATENACIÒN CON COMA (,) =============================================

print("\nCONCATENACIÒN USANDO ,")
#print("=", * 30)
# Al utilizar comas, Python permite mostrar diferentes tipos de datos sin necesidad de convertirlos a string.

print("Mi nombres es: ", nombre, " y mi documento es: ", documento)

# ================================================================================================
# ======================== CONCATENACION USANDO F-STRING =========================================

print("\nCONCATENACION USANDO F STRING")
print("=" * 30)

# Las f-string permiten insertar variables directamente dentro de un texto. 
# Se coloca la letra f antes de las comillas y las variables se escriben entre llaves {}

print("Mi nombre es: {nombre} y mi documento es: {documento}")

# ========================================================================================
# ======================== F STRING con varias variables =================================

print("\n MOSTRAR VARIAS VARIABLES CON F-STRING")
print("=" * 30)

# Las f string tambièn permiten crear textos de varias lìneas utilizando triple comilla. 

print(f"""
Nombre: {nombre}
Documento: {documento}
Direcciòn: {direccion}
¿Tiene deudas? {tiene_deudas}

""")

# Salto de lìnea en python ==================================================================
# \n represnta un salto de lìnea, salto de lìnea al inicio de texto.

print(f"\n hola , {nombre}")

# Salto de lìnea al final del texto.

print(f"Bienvenido, {nombre} a Python. \n")

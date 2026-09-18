# ==============================================================================
# ====================== SUMA DE DOS NÙMEROS CON INPUT =========================

numero1 = float(input("Ingrese el valor del primer nùmero: "))
numero2 = float(input("Ingrese el valor del segundo nùmero: "))

Suma = numero1 + numero2 # Se calcula la suma de los dos nùmeros 

print(f"La suma es: {Suma}")

# ==================== los valores que vamos a usar para la prueba son 5, 3 y el 
# resultado de la suma debe ser 8.0

# =================================================================================

print("\n EJERCICIO 2: ÀREA DE UN TRIANGULO")

base = float(input("Ingrese la base del rectàngulo: "))
altura = float(input("Ingrese la altura del rectàngulo: "))

area = base * altura # La formula es (base * altura)

print(f"El àrea del triangulo es: {area}")

# Para este ejemplo vamos a usar los valores de ejemplo 4, 6 y el resultado serà 24.0
# ======================================================================================
# EJERCICIO 3: MINUTOS O HORAS Y MINUTOS 

print("\n EJERCICIO 3: MINUTOS O HORAS Y MINUTOS")

minutos_totales = float(input("Ingrese la cantidad de minutos "))

horas = minutos_totales // 60 # division entera - horas completas. 
minutos = minutos_totales % 60 # modulo - minutos restantes. 

print(f"{minutos_totales} minutos equivalen a {horas} y {minutos} minutos")

# Vamos a usar los valores de entrada de 130 y nos dara el valor de 130 minutos
# equivalen a 2 horas y 10 minutos

# =======================================================================================
# EJERCICIO 4: CÀLCULO DEL PRECIO CON DESCUENTO... 

print("\n EJERCICIO 4: CÀLCULO DEL PRECIO CON DESCUENTO")

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100) # Valor que se descuenta. 
precio_final = precio - valor_descuento

print(f"El precio final a pagar es: {precio_final}")

# Vamos a tomar como valor de ejemplo 100000 y descuento 20.
# ===============================================================================================
# EJERCICIO 5: INTERCAMBIO DE VALORES ENTRE DOS VARIABLES =======================================

print("\n EJERCICIO 5: INTERCAMBIO DE VALORES ENTRE DOS VARIABLES")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b:"))

auxiliar = a # Guarda temporalmente el valor de a
a = b # a toma el valor de b
b = auxiliar # b tomal el valor original de A.

print(f"Despuès del intercambio: a {a}, b = {b}")

# Los valores que se van a utilizar en este ejercicio son 3 y 9 y el resultado serà a = 9.0 y b = 3.0





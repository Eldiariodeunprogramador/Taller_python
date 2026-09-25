# ====================================================================
# ====================================================================
# ============= EJERCICIO 9: FUNCIÒN RAIZ CUADRADA CON VALIDACIÒN ====
# ====================================================================
# ====================================================================
def raiz_cuadrada(n): #Def nos sirve para crear una nueva funciòn ====

    if n < 0:
        raise ValueError("No se puede calcular raiz de un nùmero negativo")
    return n ** 0.5

try:
    numero = float(input("Ingresa un nùmero: "))
    resultado = raiz_cuadrada(numero)
    print(f"Raiz cuadrada: {resultado:.4f}")
except ValueError as e:
    print(f"Error: {e}")
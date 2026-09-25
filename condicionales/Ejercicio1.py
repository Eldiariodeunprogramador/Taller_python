# Ejercicio 1: Nùmero positivo, negativo o cero. ===================
# ==================================================================

# Comenzar ingresando un numero ====================================

numero = float(input("Ingrese un nùmero: "))

if numero > 0: 
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El nùmero es cero")
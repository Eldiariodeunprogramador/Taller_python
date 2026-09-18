# EJERCICIO 5: FACTORIAL CON FOR ========================================
# SOLICITAR UN NUMERO ENTERO NO NEGATIVO Y CALCULAR SU FACTORIAL USANDO UN 
# CICLO FOR ==============================================================

numero = int(input("Ingrese un nùmero entero no negativo: "))

factorial = 1
for i in range(1, numero + 1):
    factorial = factorial * i
print(f"El factorial de {numero} es: {factorial}")
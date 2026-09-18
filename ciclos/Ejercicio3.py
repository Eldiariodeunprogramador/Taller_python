# EJERCICIO 3: CONTAR PARES CON WHILE ================================
# SOLICITAR N Y CONTAR CUANTOS NÙMEROS PARES HAY ENTRE 1 Y N USANDO UN
# CICLO WHILE... =====================================================

n  = int(input("Ingrese un numero entero positivo: ")) 

contador = 0
numero = 1

while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
        numero = numero + 1
print(f"Hay {contador} nùmeros pares entre 1 y {n}")        
# ================================================================
# EJERCICIO 1: TABLA DE MULTIPLICAR ==============================
# EJERCICIO 1: MOSTRAR LA TABLA DE MULTIPLICAR DE UN NÙMERO ======

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")

# PARA HACER LA PRUEBA DE ESTE EJERCICIO VAMOS A INGRESAR EL NÙMERO 5,
# EL RESULTADO SERA 5 X 1 = 5; 5 X 2 = 10; 5 X 10 = 50.    

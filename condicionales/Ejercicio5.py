# ==================================================================
# Solicitar tres nùmeros y determinar cual es el mayor =============
# ==================================================================

num1 = float(input("Ingresar el primer nùmero: "))
num2 = float(input("Ingrese el segundo nùmero: "))
num3 = float(input("Ingrese el tercer nùmero: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print(f"El mayor de los tres nùmeros es: {mayor}")
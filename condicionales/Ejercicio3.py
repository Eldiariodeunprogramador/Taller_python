# ===============================================================
# Solicitar un nùmero entero y determinar si es par o impar =====
# ===============================================================

numero = int(input("Ingrese un nùmero entero: "))

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
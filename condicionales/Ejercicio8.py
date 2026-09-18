# ======================================================================================
# ELABORAR UN ALGORITMO QUE SOLICITE EL NOMBRE DE UN CLIENTE Y EL VALOR TOTAL DE UNA COMPRA, Y CALCULE 
# EL DESCUENTO SEGUN EL VALOR.
# MENOS DE $100.000 - SIN DESCUENTO
# Entrada de datos
nombre = input("Nombre del cliente: ")
valor_compra = float(input("Valor total de la compra ($): "))

# Validación
if valor_compra <= 0:
    print("Error: El valor de la compra debe ser mayor a cero.")
else:
    # Determinar porcentaje de descuento
    if valor_compra < 100000:
        porcentaje = 0
    elif valor_compra < 300000:
        porcentaje = 10
    elif valor_compra < 500000:
        porcentaje = 15
    else:
        porcentaje = 20

    # Cálculos
    valor_descuento = valor_compra * (porcentaje / 100)
    total_pagar = valor_compra - valor_descuento

    # Salida final
    print(f"""
    Nombre del cliente: {nombre}
    Valor de la compra: {valor_compra:,.2f}
    Descuento aplicado: {porcentaje}
    Valor descuento: {valor_descuento:,.2f}
    Total a pagar: ${total_pagar:,.2f}    
    """)
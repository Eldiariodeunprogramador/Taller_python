# Elaborar un algoritmo que solicite el nombre de un empleado, las horas trabajadas durante el mes y el valor de cada hora.
# Las primeras 160 horas son horas normales y se pagan con la tarifa establecida. 
# Las horas por encima de 160 son horas extras y se pagan al 125% del valor de la hora normal
# Validar que las horas trabajadas y el valor de las horas sean valores positivos
# Validar un descuento de salud y pension equivalente al 8% del salario total (bruto) y obtener el salario
# neto a pagar.
# Al finalizar, debe mostrar las horas normales, las horas extras, el pago por cada una, el salario total (bruto)
# y el salario neto después del descuento.

nombre = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese horas trabajadas: "))
valor_horastrab = float(input("Ingrese el valor de las horas trabajadas: "))

# if horas_trabajadas and valor_horastrab <= 0:
# pago1 = horas_trabajadas * valor_horastrab = pago1 * 0.08
# REGISTRO DE NOTAS Y CÀLCULO DEL PROMEDIO - CICLO FOR: SOLICITA AL USARIO
# CUÀNTAS NOTAS DESEA REGISTRAR.
# RECORRER ESA CANTIDAD CON UN CICLO FOR, PIDIENDO CADA NOTA Y ACUMULANDO 
# SUS VALORES. # CALCULAR Y MOSTRAR EL PROMEDIO AL FINALIZAR EL REGISTRAR. 
# INDICAR SI EL ESTUDIANTE APROBÒ (PROMEDIO >= 3.0) O NO APROBÒ...
# SOLICITAR LA CANTIDAD DE NOTAS...

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
cantidad = int(input("¿Cuàntas notas deseas registrar? "))

# VALIDAR QUE SEA MAYOR A CERO (0)
while cantidad <= 0:
    print("Debe registrar al menos una nota. Intenta nuevamente")
    cantidad = int(input("¿Cuàntas notas desea registrar? "))

suma_notas = 0    

# RECORRER CON UN CICLO FOR PARA PEDIR Y ACUMULAR LAS NOTAS 
for i in range(1, cantidad + 1):
    nota = int(input(f"Ingrese la nota {i} "))
    suma_notas += nota 

# CALCULAR PROMEDIO...
promedio = suma_notas / cantidad

# MOSTRAR EL RESULTADO...
print(f"\n El promedio es {promedio:2f}, y el nombre del estudiante es: {nombre_estudiante}")

# DETERMINAR SI APROBÒ O REPROBO
if promedio >= 3.5:
    print("El estudiante con nombre  aprobò")
else:
    print("El estudiante NO aprobò")

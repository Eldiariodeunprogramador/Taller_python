# Elaborar un algoritmo que solicite el nombre de un estudiante y su calificación final, en una escala 
# del 0.0 al 5.0.
# Se aprueba con una nota mayor a 3.0.
# Debe validar que la calificación este dentro del rango permitido (0.0 a 5.0); si no esta entonces
# mostrar un mensaje de error y no continuar con la evaluación...
# Además de aprobado / reprobado, clasificar el desempeño: "excelente 4.5 a 5.0", "bueno 3.5 a 4.4"
# "aceptable 3.0 a 3.4" y insuficiente si es menor a 3.0.
# Al final debe mostrar el nombre del estudiante, la calificación ingresada, el resultado (aprobado / reprobado)
# y la clasificación del desempeño.
# Entrada de datos...

nombre = input("Ingrese el nombre del estudiante") # solicitar el nombre del estudiante
calificaciones = float(input("Ingrese la calificación final entre (0.0 a 50): ")) # Ingresar la calificación del estudiante.

# Validar el rango de la solicitud 

if calificaciones < 0.0 or calificaciones < 5.0:
    print("Tienes un error, la calificación debe estar entre 0.0 y 5.0")
    #Determinar el resultado que se va a mostrar en la pantalla.
else:
    if calificaciones <= 3.0:
        resultado = "APRUEBA"
    else:
        resultado = "REPRUEBA"

        # CLASIFICACIÓN DEL DESEMPEÑO
       
if 4.5 <= calificaciones <= 5.0:
     desempeno = "EXCELENTE"
elif 3.5 <= calificaciones <= 4.4:
    desempeno = "BUENO"
elif 3.0 <= calificaciones <= 3.4:
    desempeno = "ACEPTABLE"
else:
    desempeno = "INSUFICIENTE"

        # Salida final
print("\n=== Resultado Evaluación ===")
print(f"Estudiante: {nombre}")
print(f"Calificación: {calificaciones:.1f}")
# print(f"Resultado: {resultado}")
print(f"Desempeño: {desempeno}")
# PROMEDIO > 3.5... MOSTRAR SI EL ESTUDIANTE GANO, SINO EL ESTUDIANTE PERDIÓ

print("======================== SISTEMA DE CALIFICACIONES ======================================================================")
estudiante = input("Nombre del estudiante: ")
cantidad_nota = int(input("¿Cuantas notas vas a registrar? "))

promedio = 0

for i in range(cantidad_nota):
    notas = float(input(f"Ingrese nota {i+1} : "))
    promedio += notas
if (promedio/cantidad_nota) >= 3.5:
    print(f"El estudiante con nombre {estudiante} tiene un promedio de {promedio/cantidad_nota} gano 🎉🎉")
else:
    print(f" El estudiante se llama {estudiante} y su  promedio de la nota es: ", promedio/cantidad_nota, "perdió 😢😢" )    
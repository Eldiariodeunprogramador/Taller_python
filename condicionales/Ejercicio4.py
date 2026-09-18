# ================================================================
# Solicitar una nota entre (0.0) y (5.0) y clasificar el desempeño
# del estudiante... ==============================================
# ================================================================

nota = float(input("Ingrese una nota obtenida (0.0 a 5.0): "))

if nota >= 4.5: 
    print("El estudiante tuvo un desempeño superior")
elif nota >= 3.5:
    print("El estudiante tuvo un desempeño alto")
elif nota >= 3.0:
    print("El estudiante tuvo un desempeño bàsico")
else:
    print("El estudiante tuvo un desempeño bajo")
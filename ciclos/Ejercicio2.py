# ====================================================================
# SOLICITAR UN NÙMERO ENTERO POSITIVO N YY CALCULAR LA SUMA DE LOS 
# PRIMEROS N NÙMEROS NATURALES... ===================================

n = int(input("Ingrese un nùmero entero positivo: "))

suma = 0

for i in range(1, n + 1):
    suma = suma + i
print(f"La suma de los primeros {n} nùmeros naturales es : {suma}") 

# PARA HACER UNA PRUEBA DE ESTE CÒDIGO VAMOS A INGRESAR EL NÙMERO 5, Y
# VAMOS A VER EL MENSAJE: LA SUMA DE LOS PRIMEROS 5 NUMEROS NATURALES 
# ES: 15 =============================================================
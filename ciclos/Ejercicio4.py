# ===================================================================
# EJERCICIO 4: VALIDAR CONTRASEÑA ===================================
# ===================================================================
# SOLICITAR UNA CONTRASEÑA HASTA QUE SEA CORRECTA ===================

clave_correcta = "python2026"

clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")    

# PARA REALIZAR LA PRUEBA DE LA CONTRASEÑA AL EJECUTAR, VAMOS A ESCRIBIR
# PYTHON123, A CONTINUACIÒN NOS MOSTRARÀ EL MENSAJE CONTRASEÑA INCORRECTA
# SI INGRESA LA CONTRASEÑA PYTHON2026, LE MOSTRARÀ EL MENSAJE CONTRASEÑA
# CORRECTA, ACCESO CONCEDIDO. ==========================================
# ADIVINA EL NÙMERO, CICLO WHILE: GENERA UN NÙMERO ENTERO ALEATORIO ENTRE 1
# AL 10 Y SOLICITA AL USUARIO QUE INTENTE ADIVINARLO. =====================
# ========== SIMULAR UN CICLO DO... WHILE CON WHILE TRUE + BREAK, YA QUE 
# PYTHON NO TIENE ESA ESTRUCTURA NATIVA... ================================
# ========== REPETIR LA PREGUNTA MIENTRAS EL NÙMERO INGRESADO SEA DIFERENTE 
# AL NÙMERO GENERADO ======================================================
# ========== MOSTRAR UN MENSAJE DE CIERTO CUANDO EL USUARIO ADIVINE CORRECTA/
# VAMOS A DEFINIR EL NÙMERO SECRETO DIRECTAMENTE.

numero_secreto  = 7 # ESTE ES EL NUMERO SECRETO, PERO SE PUEDE CAMBIAR POR OTRO.

print("ADIVINE EL NÙMERO ENTRE 1 AL 10")

# HACER UNA SIMULACIÒN DE DO... WHILE TRUE + BREAK
while True:
    intento = int(input("Ingresa tù numero: "))

    if intento == numero_secreto:
        print(f"!Felicidades¡ Adivinaste,el nùmero es {numero_secreto} ")
        break
    else:
        print("Numero incorrecto, intenta nuevamente... \n")

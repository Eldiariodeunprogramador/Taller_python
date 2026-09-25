# CUENTA REGRESIVA - CICLO WHILE: SOLICITA AL USUARIO UN NÙMERO ENTERO 
# MAYOR QUE CERO (0).
# RECORRER CON UN CICLO WHILE DESDE ESE NÙMERO HASTA CERO (0), MOSTRANDO
# CADA VALOR EN LA CONSOLA.
# MOSTRAR UN MENSAJE INDICANDO QUE LA CUENTA REGRESIVA A TERMINADO. 

# SOLICITAR NÙMERO MAYOR QUE 0

numero = int(input("Ingrese un numero entero mayor que 0: "))

# VALIDAR QUE SEA MAYOR QUE CERO (0)
while numero <= 0:
    print("El numero debe ser mayor que 0, intente nuevamente")
    numero = int(input("Ingrese un nùmero entero mayor que cero (0): "))

# RECORRER DESDE EL NÙMERO DESDE CERO (0)
contador = numero
while contador >= 0:
    print(contador)
    contador -= 1
print("La cuenta regresiva ha terminado")    

# NUMEROS IMPARES - CICLO FOR: RECORRE CON UN CICLO FOR LOS NÙMEROS ENTEROS
# MAYOR QUE CERO (0).
# RECORRER CON UN CICLO WHILE DESDE ESE NÙMERO HASTA CERO (0), MOSTRANDO CADA
# VALOR EN LA CONSOLA.
# MOSTRAR UN MENSAJE INDICANDO QUE LA CUENTA REGRESIVA HA TERMINADO...

print("Nùmeros impares del 1 al 100: ")

numero = int(input("Ingrese un nùmero: "))

for numero in range(1, 100):
    if numero % 2 != 0: # Si el resto no es 0, es par.
        print(numero)
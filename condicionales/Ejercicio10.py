# ===============================================================
# Elaborar un algoritmo que solicite el nombre y la edad de una 
# persona y determine si es mayor o menor de edad: 
#
# ***** Se considera mayor de edad a partir de los 18 años *****
# ***** Validar que la edad ingresada no sea un valor negativo, si
# lo es, mostrar un mensaje de error... ***** 
# ***** Si la persona es menor de edad, calcular y mostrar cuàntos
# años le faltan para cumplir la mayorìa de edad... *****
# ***** Al finalizar, debe mostrar el nombre, la edad ingresada y el 
# resultado correspondiente... *****


nombre = input("Por favor ingrese su nombre: ") # Solicitar el nombre del usuario.
edad = int(input("Ingrese su edad: ")) # Solicitar la edad del usuario.

# Validar si la edad es negativa. 

if edad < 0: 
    print("Error la edad no puede ser un valor negativo")
else:
    # Determinar condición
    mayor_edad = 18 # Declaro una variable indicando que es mayor de edad.
    if edad >= mayor_edad:
        resultado = mayor_edad 
    else:
        anos_faltantes = mayor_edad - edad
        resultado = f"Es menor de edad, le faltan {anos_faltantes} años para la mayoría de edad"

        # Salida final
    print("\n=== RESULTADO =================================")
    print("\n===============================================")
    print(f"Nombre: {nombre}")
    print(f"Edad ingresada: {edad} años")
    print(resultado)
    print("\n===============================================")
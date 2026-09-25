# ======================================================================================================================================
# =============================================EJERCICIOS CON 

while True:
    try:
        cantidad_notas = int(input("CUANTAS NOTAS QUIERES REGISTRAR: "))
        lista_notas = [] # Se crea una lista vacia...
        
        for i in range(cantidad_notas):
            try: 
                nota = float(input("INGRESE NOTA: "))
                lista_notas.append(nota)
            except ValueError:
                print("Nota invalida")
        print("NOTA REGISTRADA CON EXito: ", lista_notas)
        promedio = sum(lista_notas) / len (lista_notas)
        print(f"Promedio: {promedio}")
        if promedio <= 2:
            print(f"El promedio de las notas es: {promedio} muy mal promedio")
        elif promedio <= 3:
            print(f"El promedio de las notas es: {promedio} el alumno tiene promedio medio ")
        elif promedio <= 4: 
            print(f"EL promedio es {promedio} su nota es aceptable")
        elif promedio <= 5:
            print(f"El promedio es {promedio} las notas son buenas")
        
        
    except ValueError:
        print("Ingrese una cantidad valida 📝📝📝")            
       
        
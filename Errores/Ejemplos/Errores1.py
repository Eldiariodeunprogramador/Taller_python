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
    except ValueError:
        print("Ingrese una cantidad valida 📝📝📝")            
       
        
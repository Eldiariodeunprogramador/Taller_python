lista_perros = [] # Esta es una lista vacia 
lista_gatos = [] # Esta es una lista vacia. 

while True:
    
    preguntar = input("""
    1) Registrar perritos 🐩  
    2) Registrar gatos    🐈 
    3) Listado de perritos 🐾
    4) Listado de gatos    😻   
    5) Salir 🚪   
    """)  # Cerrar el print de multiples 
    
    if preguntar == 1:
        nombre_perro = input("Cual es el nombre del perro: ")
        lista_perros.append(nombre_perro)
        print("El perro ha sido registrado con exito")
    elif preguntar == 2:
        nombre_gato = input("Cual es el nombre del gato: ")
        lista_gatos.append(nombre_gato)
        print(f"El gato ha sido registrado con exitoso")
    elif preguntar == 3:
        print("Listar todos los perros", lista_perros)
    elif preguntar == 4:
        print("Listar todos los gatos", lista_gatos)
    elif preguntar == 5:
        print("Saliendo del sistema")
        break
    else:
        print("Opción invalida")
        break
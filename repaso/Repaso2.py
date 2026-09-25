lista_productos = [] # Esta es una lista vacia....

cantidad = int(input("Cantidad de productos a comprar: "))

for i in range(cantidad):
    producto = input(f"Nombre del producto  {i + 1}: ")
    # Agregar producto a la lista....
    lista_productos.append(producto)
print(f"Los productos comprados son: {lista_productos}")    
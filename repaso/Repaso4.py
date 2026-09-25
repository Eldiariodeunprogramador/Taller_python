print("---------------------- TIENDA DONDE ELI ----------------------")
print("POR FAVOR INGRESE LA SIGUIENTE INFORMACIÓN:")

cliente = input("Ingrese su nombre: ")
producto = input("Ingrese el producto que desea comprar: ")
cantidad = int(input("Ingrese la cantidad que desea comprar: "))
precio = float(input("Ingrese el precio del producto: "))

# VARIABLE PARA PREGUNTAR SI LA COMPRA ES A DOMICILIO
domicilio = input("¿La compra es con entrega a domicilio? (SI/NO): ")

# CÁLCULO DEL TOTAL PARCIAL
total_sin_envio = cantidad * precio
costo_envio = 0

# CONDICIÓN SI NO ES DOMICILIO
if domicilio.upper() == "NO":
    print("\n====== RESUMEN DE LA COMPRA ======")
    print(f"Cliente: {cliente}")
    print(f"Producto: {producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${precio:,.2f}")
    print(f"Subtotal: ${total_sin_envio:,.2f}")
    print("Costo de envío: $0.00")
    print(f"TOTAL A PAGAR: ${total_sin_envio:,.2f}")
    print("Gracias por su compra 😊😊")

# CONDICIÓN SI SÍ ES DOMICILIO
elif domicilio.upper() == "SI":
    direccion = input("Ingrese la dirección de entrega: ")
    # Puedes ajustar este valor según tu regla de negocio
    costo_envio = 15000  
    total_con_envio = total_sin_envio + costo_envio
    
    print("\n====== RESUMEN DE LA COMPRA CON DOMICILIO ======")
    print(f"""
          CLIENTES: {cliente}
          PRODUCTO: {producto}
          CANTIDAD: {cantidad}
          PRECIO UNITARIO: {precio}
          SUBTOTAL: {total_con_envio}
          COSTO DE ENVIO: {costo_envio}
          DIRECCIÓN DE ENTREGA: {direccion}
          TOTAL A PAGAR: {total_con_envio}
          
          GRACIAS POR SU COMPRA 💳🛒
          
          """)
    
    #print(f"Cliente: {cliente}")
    #print(f"Producto: {producto}")
    #print(f"Cantidad: {cantidad}")
    #print(f"Precio unitario: ${precio:,.2f}")
    #print(f"Subtotal: ${total_sin_envio:,.2f}")
    #print(f"Costo de envío: ${costo_envio:,.2f}")
    #print(f"Dirección de entrega: {direccion}")
    #print(f"TOTAL A PAGAR: ${total_con_envio:,.2f}")
    #print("Gracias por su compra 😊😊")

# RESPUESTA INVÁLIDA
else:
    print("\n⚠️ Respuesta no válida. Por favor responda con SI o NO.")
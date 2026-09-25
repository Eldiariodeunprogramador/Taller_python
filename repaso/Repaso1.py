# ==============================================================================================================================
# ==============================================================================================================================
# ================ VAMOS A CREAR UN ALGORITMO QUE PERMITA VENDER PRODUCTOS =====================================================
# ================ NOMBRE_CLIENTE, PRODUCTO, CANTIDAD, PRECIO, DOMICILIO (PREGUNTAR: "MUNICIPIO, BAQRRIO, DIRECCIÓN") ==========
# ================ MEDELLIN: 5000, BELLO: 8000, ITAGUI: 40.000 =================================================================")


print("====================== TIENDA DONDE ELI ===================================")
print("POR FAVOR INGRESE LA SIGUIENTE INFORMACIÓN: ")

cliente = input("Ingrese su nombre: ")
producto = input("Ingrese el producto que desea comprar: ")
cantidad = int(input("Ingrese la cantidad que desea comprar: "))
precio = float(input("Ingrese el precio del producto: "))

# VARIABLE PARA PREGUNTAR SI LA COMPRA ES ES A DOMICILIO ..............................
domicilio = input("Ingrese su domicilio: ")

# CREAR UNA CONDICIÓN PARA VERIFICAR QUE RESPONDIO EL USUARIO ==========================
# .upper() SIRVE PARA CONVERTIR EN MAYUSCULAS  .lower() SIRVE PARA CONVERTIR EN MINUSCULAS.

if domicilio.upper() == "NO":
    print("====== RESUMEN DE LA COMPRA ================")
    print(f""" 
          
          Cliente: {cliente}
          Producto: {producto}
          Cantidad: {cantidad}
          Precio: {precio}  
          Total: {cantidad * precio}
          
          Gracias por su compra 👌👌👌         
          
          """)
   
elif domicilio.upper() == "SI":
    direccion = input("Ingrese el municipio de envio (Medellín, Itagui, Bello)")
    valor_domicilio = 0
    
    if direccion.lower() == "Medellin":
        valor_domicilio = 5000
    elif direccion.lower() == "Itagui":
        valor_domicilio = 10000
    elif direccion.lower() == "Bello":
        valor_domicilio = 8000
    else:
        print("Dirección invalida")

# MOSTRAR RESUMEN DE VENTA

print("==================================== RESUMEN DE LA COMPRA =============================================")        
print(f"""
      Cliente: {cliente}
      Producto: {producto}
      Cantidad: {cantidad}
      Precio: {precio}
      Subtotal {cantidad * precio} 
      Domicilio {valor_domicilio}
      Total a pagar: {valor_domicilio + (cantidad * precio)}
      
      👌👌👌 GRACIAS POR SU COMPRA 😊😊😊😊😊
      
      """)

    
   

   
   
   
   
   
   
   
   
   
   
   
   
   
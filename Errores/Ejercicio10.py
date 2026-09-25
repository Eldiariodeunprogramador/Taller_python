# ====================================================================
# ====================================================================
# ============= EJERCICIO 10: ACUMULAR NÙMEROS HASTA FIN =============
# ====================================================================
# ====================================================================

suma =0
contador = 0

while True:
    entrada = input("Ingrese un nùmero o escriba 'fin' para terminar: ")

    if entrada.lower() == 'fin':
        break

    try: 
        valor = float(entrada)
        suma += valor
        contador += 1
    except ValueError:
        print(f"{entrada} no es un nùmero vàlido - ignorado ")

if contador > 0:
    promedio = suma / contador
    print(f"\n valores aceptados: {contador}")        
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:2f}")
else:
    print("\n No se ingresaron valores vàlidos")
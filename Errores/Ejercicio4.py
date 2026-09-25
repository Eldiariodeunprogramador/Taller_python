# ============================================================
# ============ EJERCICIO 4: SOLICITAR UN DATO VÀLIDO HASTA ===
# ============ QUE EL USUARIO LO INGRESE CORRECTAMENTE =======
# ============ COMBINAR UN CICLO WHILE CON TRY / EXCEPT ======
# ============ PARA PEDIRLE AL USUARIO QUE REINTENTE HASTA ===
# ============ INGRESAR UN VALOR VÀLIDO ======================

while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota < 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break # Sale del ciclo si el valor es vàlido...

    except ValueError as e:
        print(f"Entrada invàlida: {e}. Intente de nuevo")

print(f"Nota registrada: {nota}")   

# ===============================================================
# ========== ENTRADA: -1, abc, 6, 4.5 ... ENTRADA INVÀLIDA * 3 ==
# ========== NOTA REGISTRADA: 4.5 ===============================
# ===============================================================
# ===============================================================

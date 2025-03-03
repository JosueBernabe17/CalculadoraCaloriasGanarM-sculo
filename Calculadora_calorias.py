def calcular_calorias():
    print("💪 Calculadora de calorías para ganar masa muscular")

    # Solicitar datos al usuario
    edad = int(input("¿Cuál es tu edad?: "))
    género = input("¿Eres hombre o mujer (h/m)?: ").lower()
    peso = float(input("¿Cuál es tu peso en kg?: "))
    altura = float(input("¿Cuál es tu altura en cm?: "))
    actividad_fisica = input("¿Cuál es tu nivel de actividad física (sedentario, ligero, moderado, activo, muy activo)?: ").lower()

    # Calcular BMR (Tasa Metabólica Basal)
    if género == "h":
        BMR = 10 * peso + 6.25 * altura - 5 * edad + 5
    elif género == "m":
        BMR = 10 * peso + 6.25 * altura - 5 * edad - 161
    else:
        print("⚠️ Género no válido")
        return

    # Validar nivel de actividad física
    factores = {
        "sedentario": 1.2,
        "ligero": 1.375,
        "moderado": 1.55,
        "activo": 1.725,
        "muy activo": 1.9
    }

    if actividad_fisica not in factores:
        print("⚠️ Nivel de actividad no válido. Intenta de nuevo.")
        return

    # Calcular calorías necesarias
    calorias = BMR * factores[actividad_fisica]
    print("\n📌 Resultado:")
    print(f"\n🔥 Debes consumir aproximadamente {calorias:.2f} calorías diarias para aumentar masa muscular.")
    print("💪 ¡A comer proteína y a entrenar duro!")

# Llamar a la función para ejecutar el cálculo
calcular_calorias()




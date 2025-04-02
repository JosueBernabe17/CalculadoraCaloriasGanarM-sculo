class CalculadoraCalorias:
    def __init__(self):
        """Inicializa la calculadora y ejecuta el cálculo"""
        self.calcular_calorias()

    def calcular_calorias(self):
        
        print("💪 Calculadora de calorías para ganar masa muscular\n")

        usuario = input("Ingrese su Nombre?: ").lower()  

        while True:

            
            try:
                edad = int(input("¿Cuál es tu edad?: "))
                if edad <= 0:
                    print("⚠️ La edad debe de ser un número positivo.")
                    continue
                break  # Salimos del bucle si el dato es válido
            except ValueError:
                print("❌ Error: Ingresa un número válido para la edad.")

        while True:
            try:
                peso = float(input("¿Cuál es tu peso en kg?: "))
                if peso <= 0:
                    print("⚠️ El peso debe de ser un número positivo.")
                    continue
                break
            except ValueError:
                print("❌ Error: Ingresa un número válido para el peso.")

        while True:
            try:
                altura = float(input("¿Cuál es tu altura en cm?: "))
                if altura <= 0:
                    print("⚠️ La altura debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("❌ Error: Ingresa un número válido para la altura.")

        while True:
            género = input("¿Eres hombre o mujer (h/m)?: ").lower()
            if género in ["h", "m"]:
                break
            print("⚠️ Género no válido. Debe ser 'h' o 'm'.")

        # Validar nivel de actividad física           
        factores = {
            "sedentario": 1.2,
            "ligero": 1.375,
            "moderado": 1.55,
            "activo": 1.725,
            "muy activo": 1.9
        }

        while True:    
            actividad_fisica = input(f"¿Cuál es tu nivel de actividad física {usuario} (sedentario, ligero, moderado, activo, muy activo)?: ").lower()
            if actividad_fisica in factores:
                break
            print("⚠️ Nivel de actividad no válido. Intenta de nuevo.")

        # Calcular BMR (Tasa Metabólica Basal)
        BMR = (10 * peso + 6.25 * altura - 5 * edad + (5 if género == "h" else -161))
        calorias = BMR * factores[actividad_fisica]

        print("\n📌 Resultado:")
        print(f"\n🔥 {usuario} Debes consumir aproximadamente {calorias:.2f} calorías diarias para aumentar masa muscular.")
        print(f"💪 ¡A comer proteína y a entrenar duro! {usuario}")

# Llamar a la función para ejecutar el cálculo
if __name__ == "__main__":
    CalculadoraCalorias()

def calcular_horas_extra(horas_trabajadas, horas_normales):
    # Calcula las horas extra trabajadas
    horas_extra = horas_trabajadas - horas_normales
    return horas_extra if horas_extra > 0 else 0

def calcular_pago_extra(horas_extra, tarifa_hora):
    # Calcula el pago por las horas extra trabajadas
    pago_extra = horas_extra * tarifa_hora * 1.5  # Se asume una tarifa de horas extras del 50% más
    return pago_extra

def main():
    try:
        horas_normales = float(input("Ingrese las horas normales trabajadas: "))
        horas_trabajadas = float(input("Ingrese las horas totales trabajadas: "))
        tarifa_hora = float(input("Ingrese la tarifa por hora: "))

        horas_extra = calcular_horas_extra(horas_trabajadas, horas_normales)
        pago_extra = calcular_pago_extra(horas_extra, tarifa_hora)

        print(f"Horas extra trabajadas: {horas_extra}")
        print(f"Pago por horas extra: ${pago_extra:.2f}")

    except ValueError:
        print("Error: Por favor ingrese números válidos.")

if __name__ == "__main__":
    main()

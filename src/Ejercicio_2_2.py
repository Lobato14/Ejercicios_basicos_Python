# Escribe un programa para pedirle al usuario las horas de trabajo y el precio
# por hora y calcule el importe total del servicio.

def calcular_importe(horas, precio):
    if horas < 0 or precio < 0:
        return "Las horas y el precio deben ser números positivos"
    else:
        importe = horas * precio
        return importe
    
if __name__ == "__main__":
    horas = int(input("Escribe las horas trabajadas: "))
    precio = int(input("Escribe el precio trabajado: "))
    if horas < 0 or precio < 0:
        print("Las horas y el precio deben ser números positivos")
    else:
        resultado = calcular_importe(horas, precio)
        print("El importe total del servicio es de", resultado)
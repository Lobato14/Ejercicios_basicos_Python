# Escribe un programa para pedirle al usuario las horas de trabajo y el precio
# por hora y calcule el importe total del servicio.

def calcular_importe(horas, precio):
    importe = horas * precio
    return importe

if __name__=="__main__":
    horas = int(input("Escribe las horas trabajadas: "))
    precio = int(input("Escribe el precio trabajado: "))
    print(calcular_importe(horas, precio))
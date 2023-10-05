# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

def resultado_operacion():
    operacion = (3+2/(2*5))**2
    operacion_redondeada = round(operacion, 2)
    return "El resultado es " + str(operacion_redondeada)

if __name__=="__main__":
    print(resultado_operacion())
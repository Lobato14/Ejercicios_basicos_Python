# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del
# país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un
# número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

def obtener_numero_sin_digitos(numero):
    partes = numero.split("-") 
    if len(partes) >= 2 and partes[0] == "+34":
        numSinDigitos = int(partes[1])
        return numSinDigitos
    else:
        return None

numero = input("Escriba un número de teléfono: ")
resultado = obtener_numero_sin_digitos(numero)

if resultado is not None:
    print("Su número sin dígitos es", resultado)
else:
    print("El número de teléfono no tiene el formato correcto.")
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del precio introducido.

def separar_euros_y_centimos(precio):
    # Separamos los euros y centimos con split
    euros, centimos = precio.split('.')
    # Convertir las partes en enteros con int
    euros = int(euros)
    centimos = int(centimos)
    return euros, centimos

if __name__ == "__main__":
    precio = input("Escribe el precio del producto en euros con dos decimales: ")
    try:
        euros, centimos = separar_euros_y_centimos(precio)
        print("Euros:", euros)
        print("Céntimos:", centimos)
    except ValueError:
        print("Por favor, introduce un precio válido en el formato correcto.")
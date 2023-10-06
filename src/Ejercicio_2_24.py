# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del precio introducido.

def separar_euros_y_centimos(precio):
    try:
        if precio == "":
            raise ValueError("El precio no puede estar vacío.")
        precio_float = float(precio)
        if precio_float < 0:
            raise ValueError("El precio debe ser un número positivo.")
        euros, centimos = str(precio_float).split('.')
        euros = int(euros)
        centimos = int(centimos)
        return euros, centimos
    except ValueError as e:
        print(e)
        return None, None

if __name__ == "__main__":
    try:
        precio = float(input("Escribe el precio del producto en euros con dos decimales: "))
        euros, centimos = separar_euros_y_centimos(precio)
        if euros is not None and centimos is not None:
            print("Euros:", euros)
            print("Céntimos:", centimos)
    except ValueError:
        print("Por favor, introduce un precio válido en el formato correcto.")
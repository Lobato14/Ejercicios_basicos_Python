# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla
# una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
# unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def caracteristProducto(nombre, precio, numUnidades):
    if numUnidades <= 0:
        return "La operación no es válida porque has escrito números negativos"
    else:
        costoTotal = precio * numUnidades
        return costoTotal

if __name__ == "__main__":
    nombre = input("Escribe el nombre del producto: ")
    precio = float(input("Escribe el precio del producto: "))
    numUnidades = int(input("Escribe el numero de unidades: "))
    
    costoTotal = caracteristProducto(nombre, precio, numUnidades)
    
    print("\nNombre del producto: {}".format(nombre))
    print("Precio: {:.2f}".format(precio))
    print("Unidades: {}".format(numUnidades))
    print("Costo total: {:.2f}".format(costoTotal))
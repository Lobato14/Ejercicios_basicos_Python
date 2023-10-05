# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
# y muestre por pantalla cada uno de los productos en una línea distinta.

def mostrar_lista_compra(lista_compra):
    productos = lista_compra.split(",")
    resultado = ""
    for producto in productos:
        resultado += producto.strip() + "\n"
    return resultado


if __name__ == "__main__":
    lista_compra = input("Escriba los productos de una cesta de la compra, separados por comas: ")
    mostrar_lista_compra(lista_compra)

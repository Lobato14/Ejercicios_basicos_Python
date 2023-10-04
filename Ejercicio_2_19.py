# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
# introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en
# mayúsculas y n es el número de letras que tienen el nombre.

def ponerMay_NLetras(nombreMay):
    nombreMay = nombreMay.upper()
    numLetras = len(nombreMay)
    return "Nombre en mayúsculas: " + nombreMay + "\nNúmero de letras: " + str(numLetras)

if __name__ == "__main__":
    nombre = input("¿Cuál es su nombre?: ")
    texto = ponerMay_NLetras(nombre)
    print(texto)
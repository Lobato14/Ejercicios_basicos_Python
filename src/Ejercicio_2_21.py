# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla
# la frase invertida.

def fraseInvertida(frase):
    palabras = frase.split()
    if len(palabras) < 2:
        return "La frase debe contener al menos dos palabras."
    palabrasInv = reversed(palabras)
    frase_invertida = " ".join(palabrasInv)
    return frase_invertida

if __name__ == "__main__":
    frase = input("Escriba una frase: ")
    texto = fraseInvertida(frase)
    print(texto)
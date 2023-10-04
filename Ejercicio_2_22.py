# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por
# pantalla la misma frase pero con la vocal introducida en mayúscula.

def convertir_vocal_mayuscula(frase, vocal):
    vocal_minuscula = vocal.lower()  # Convertir la vocal a minúscula
    vocal_mayuscula = vocal.upper()
    frase_con_vocal_mayuscula = frase.replace(vocal_minuscula, vocal_mayuscula)
    return frase_con_vocal_mayuscula

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    vocal = input("Escribe una vocal: ")
    # Verificar si la entrada del usuario es una sola letra
    if len(vocal) == 1 and vocal.isalpha():
        resultado = convertir_vocal_mayuscula(frase, vocal)
        print(resultado)
    else:
        print("Por favor, introduce una sola letra como vocal.")
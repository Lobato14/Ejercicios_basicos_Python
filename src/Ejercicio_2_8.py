# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

def sumar_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

if __name__ == "__main__":
    numeros = [int(input("Escribe un número: ")) for _ in range(3)]
    resultado = sumar_numeros(numeros)
    print("La suma de sus números es", resultado)
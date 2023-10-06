# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma
# de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada
# de la siguiente forma

def suma_enteros(numero):
    if numero < 0:
        return "El número entero debe ser positivo"
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma

if __name__ == "__main__":
    numero = int(input("Escribe un numero entero positivo: "))
    resultado = suma_enteros(numero)
    print("La suma de sus números es " + str(resultado))
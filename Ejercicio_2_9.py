# ¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

def suma_numeros():
    suma = int(input("Ingresa el primer número: ")) + int(input("Ingresa el segundo número: ")) + int(input("Ingresa el tercer número: "))
    return "La suma de sus números es de " + str(suma)

if __name__ == "__main__":
    print("Ingresa tres números: ")
    print(suma_numeros())
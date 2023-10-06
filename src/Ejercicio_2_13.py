# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS:
# "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos
# por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

def division_prog(numero1, numero2):
    if numero2 == 0:
        return "La división por cero no está permitida."
    elif numero1 < 0 or numero2 < 0:
        return "La división no se puede realizar correctamente debido a números negativos."
    else:
        cociente = numero1 // numero2
        resto = numero1 % numero2
        mensaje = f"La división de {numero1} entre {numero2} da un cociente {cociente} y un resto {resto}."
        return mensaje

if __name__ == "__main__":
    numero1 = int(input("Escribe un número entero: "))
    numero2 = int(input("Escribe otro número entero: "))
    print(division_prog(numero1, numero2))



# Suponiendo que se han ejecutado las siguientes sentencias de asignación:
#
ancho = 17
alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas
# en el intérprete:
#
# 1. ancho / 2
# 2. ancho // 2
# 3. alto / 3

# El valor de la expresión ancho / 2 es 8.5, y su tipo es float.
# El valor de la expresión ancho // 2 es 8, y su tipo es int.
# El valor de la expresión alto / 3 es 4.0, y su tipo es float.

def resultado_parte1(ancho):
    resultado1 = ancho / 2
    return "El primer resultado es " + str(resultado1)

def resultado_parte2(ancho):
    resultado2 = ancho // 2
    return "El segundo resultado es " + str(resultado2)

def resultado_parte3(alto):
    resultado3 = alto / 3
    return "El tercer resultado es " + str(resultado3)

if __name__ == "__main__":
    ancho = float(input("Escribe el valor del ancho: "))
    alto = float(input("Escribe el valor del alto: "))

    print(resultado_parte1(ancho))
    print(resultado_parte2(ancho))
    print(resultado_parte3(alto))
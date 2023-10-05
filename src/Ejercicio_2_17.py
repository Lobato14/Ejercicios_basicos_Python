# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en
# líneas distintas el nombre del usuario tantas veces como el número introducido.

def nombreVeces(nombre, numero):
    cadena = ""
    if not nombre.strip():  # Verifica si el nombre contiene solo espacios en blanco
        return cadena
    if numero > 0:
        for contador in range(numero):
            cadena += nombre + "\n"
    return cadena 

if __name__ == "__main__":
    # Entrada 
    nombre = input("Escriba su nombre: ")
    numero = int(input("Escriba un número entero: "))
    # Procesa
    texto = nombreVeces(nombre, numero)
    # Salida a consola
    print(texto)
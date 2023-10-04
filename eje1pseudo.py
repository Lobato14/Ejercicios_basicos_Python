# Leer un número hasta que esté entre el rango 1..10
# Solucionar para que no de decimales(que sea un float)
def leeNumero() -> int:
    # Lee un dato por pantalla hasta que sea un número. Retorna el número.
    datoEntrada = input("Introduce el número: ")
    while not datoEntrada.isdigit():
        datoEntrada = input("Introduce el numero: ")
    return int(datoEntrada)
def muestraResultado(numero):
    # Muestra el resultado por consola
    print("El número", numero, "es correcto")
def esCorrecto(numero:int) -> bool:
    # Devuelve True si cumple la condición
    return numero in range(1, 11)
# Lee el número
numero = leeNumero()
# Procesa
while not esCorrecto(numero):
    numero = leeNumero()
# Muestra salida
muestraResultado(numero)
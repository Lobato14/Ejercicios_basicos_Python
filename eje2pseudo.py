def leeNumero() -> int:
    # Lee un dato por pantalla hasta que sea un número. Retorna el número.
    datoEntrada = input("Introduce el número: ")
    while not datoEntrada.isdigit():
        datoEntrada = input("Introduce el numero: ")
    return int(datoEntrada)

def muestraResultado(serie):
    for numero in serie:
        print(numero)

def generarSerie(menor, mayor):
    serie = []
    for numero in range(menor, mayor + 1):
        serie.append(numero)
    return serie

# Lectura
print("Primer numero: \n")
numero1 = leeNumero()
print("Segundo número:\n")
numero2 = leeNumero()

# Procesamiento
if numero1 < numero2:
    menor = numero1
    mayor = numero2
else:
    menor = numero2
    mayor = numero1

serie = generarSerie(menor, mayor)

# Salida
muestraResultado(serie)
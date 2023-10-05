# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido
# a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el
# primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

interes = 0.4

def cantDeposAnual(cantDepos):
    for contador in range(3):
        cantDepos += cantDepos * interes
        print("La cantidad del año", contador + 1, "es", round(cantDepos, 2))
    return cantDepos

if __name__ == "__main__":
    cantDepos = float(input("Escribe la cantidad depositada: "))
    resultado = cantDeposAnual(cantDepos)
    print("El monto total después de 3 años es:", round(resultado, 2))
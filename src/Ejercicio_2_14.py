# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
# la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
# que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será
# enviado.

peso_payaso = 112
peso_muneca = 75

def calculo_peso(num_payasos, num_munecas):
    if num_munecas < 0 or num_payasos < 0:
        return "El numero de payasos o muñecas no pueden ser menores a 0."
    # Sumar el peso de los payasos y muñecas vendidos
    peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)
    # Convertir el peso total a kilogramos (1 kg = 1000 g)
    peso_total_kg = peso_total / 1000
    return peso_total_kg

if __name__ == "__main__":
    num_payasos = int(input("Ingrese el número de payasos vendidos: "))
    num_munecas = int(input("Ingrese el número de muñecas vendidas: "))
    print("El peso total del paquete es de", round(calculo_peso(num_payasos, num_munecas), 2), "kg")
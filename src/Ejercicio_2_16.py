# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como
# una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

def calcular_costo_pan(no_pan_Dia):
    if no_pan_Dia <=0 :
        return "El numero de barras de pan vendidas no puede ser menor o igual a 0."
    pvpPan = 3.49
    descuento = 0.6
    calcDesc = round(pvpPan * descuento, 2)
    costo_total = (pvpPan - calcDesc) * no_pan_Dia
    return pvpPan, calcDesc, round(costo_total, 2)

if __name__ == "__main__":
    no_pan_Dia = int(input("Número de barras vendidas que no son del día: "))
    precio_pan, descuento, costo_total = calcular_costo_pan()
    print("Precio de una barra de pan:", precio_pan, "€")
    print("Descuento por ser fresca:", descuento, "€")
    print("Coste total de las barras no frescas:", costo_total, "€")
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
# el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan
# con un solo carácter.

def obtener_fecha_nacimiento(fecha_nacimiento):
    dia, mes, anio = fecha_nacimiento.split("/")
    # Con zfill nos aseguramos de que tanto el día como el mes tengan al menos dos caracteres rellenando con ceros a la
    # izquierda si es necesario.
    dia = dia.zfill(2)
    mes = mes.zfill(2)
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)
    return dia, mes, anio

if __name__ == "__main__":
    fecNac = input("Escriba su fecha de nacimiento (DD/MM/AAAA): ")
    dia, mes, anio = obtener_fecha_nacimiento(fecNac)
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)
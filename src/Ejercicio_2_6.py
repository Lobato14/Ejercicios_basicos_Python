# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha
# pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)

tipoIVA = 0.10

def calcular_pvp(importFinal):
    if importFinal < 0:
        return "El importe final del articulo no puede ser un numero negativo"
    prodSinIVA = importFinal / (1 + tipoIVA)
    ivaPagado = importFinal - prodSinIVA
    prodSinIVA_redondeado = round(prodSinIVA, 2)
    ivaPagado_redondeado = round(ivaPagado, 2)
    return "El artículo sin IVA es de " + str(prodSinIVA_redondeado) + "\nEl IVA pagado es de " + str(ivaPagado_redondeado)

if __name__ == "__main__":
    importFinal = float(input("Escribe el importe final del artículo: "))
    print(calcular_pvp(importFinal))
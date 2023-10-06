# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a
# aplicar y calcule e imprima por pantalla el precio final del artículo.

def calcular_pvp_IVA(importSinIVA, tipIVA):
    if importSinIVA < 0 or tipIVA < 0:
        return "El importe del producto sin IVA y el tipo de IVA a aplicar no puede ser negativos"
    pvpFinal = importSinIVA * (1 + tipIVA)
    return "El precio final del producto es " + str(round(pvpFinal, 3))

if __name__ == "__main__":
    importSinIVA = float(input("Escriba el importe sin iva: "))
    tipIVA = float(input("Escriba el tipo de IVA a aplicar: "))
    print(calcular_pvp_IVA(importSinIVA, tipIVA))
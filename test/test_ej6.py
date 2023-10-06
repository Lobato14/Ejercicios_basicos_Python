from src.Ejercicio_2_6 import calcular_pvp

def test_calculo_pvp():
    assert calcular_pvp(121) == "El artículo sin IVA es de 110.0\nEl IVA pagado es de 11.0"
    assert calcular_pvp(-50) == "El importe final del articulo no puede ser un numero negativo"
    assert calcular_pvp(0) == "El artículo sin IVA es de 0.0\nEl IVA pagado es de 0.0"

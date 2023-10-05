from Ejercicio_2_6 import calcular_pvp

def test_calculo_pvp():
    assert calcular_pvp(121) == "El artículo sin IVA es de 110.0\nEl IVA pagado es de 11.0"
    assert calcular_pvp(50) == "El artículo sin IVA es de 45.45\nEl IVA pagado es de 4.55"
    assert calcular_pvp(75.75) == "El artículo sin IVA es de 68.86\nEl IVA pagado es de 6.89"

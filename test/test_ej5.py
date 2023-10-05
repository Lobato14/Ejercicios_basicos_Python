from Ejercicio_2_5  import calcular_pvp_IVA

def test_calculo_pvp_IVA():
    assert calcular_pvp_IVA(2.5, 1.21) == "El precio final del producto es 3.025"
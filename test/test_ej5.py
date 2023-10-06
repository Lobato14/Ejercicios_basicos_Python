from src.Ejercicio_2_5  import calcular_pvp_IVA

from src.Ejercicio_2_5 import calcular_pvp_IVA

def test_calculo_pvp_IVA():
    assert calcular_pvp_IVA(2.5, 0.21) == "El precio final del producto es 3.025"
    assert calcular_pvp_IVA(-2.5, 0.21) == "El importe del producto sin IVA y el tipo de IVA a aplicar no puede ser negativos"
    assert calcular_pvp_IVA(2.5, -0.21) == "El importe del producto sin IVA y el tipo de IVA a aplicar no puede ser negativos"
from src.Ejercicio_2_14 import calculo_peso

def test_calculo_peso():
    assert calculo_peso(5, 3) == 0.785
    assert calculo_peso(0, 0) == 0.0
    assert calculo_peso(10, 10) == 1.87
    assert calculo_peso(100, 200) == 26.2
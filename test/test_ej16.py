from src.Ejercicio_2_16 import calcular_costo_pan

def test_calculo_costo_pan():
    assert calcular_costo_pan(5) == (3.49, 2.09, 7.0)
    assert calcular_costo_pan(0) == "El numero de barras de pan vendidas no puede ser menor o igual a 0."
    assert calcular_costo_pan(-5) == "El numero de barras de pan vendidas no puede ser menor o igual a 0."
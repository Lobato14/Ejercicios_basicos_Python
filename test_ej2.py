from Ejercicio_2_2 import calcular_importe

def test_calcular_importe():
    assert calcular_importe(5, 10) == 50
    assert calcular_importe(0, 20) == 0
    assert calcular_importe(10, 10) == 100
from src.Ejercicio_2_2 import calcular_importe

def test_calcular_importe():
    assert calcular_importe(0, 100) == 0
    assert calcular_importe(5, 20) == 100
    assert calcular_importe(-1, -15) == "Las horas y el precio deben ser números positivos"
    assert calcular_importe(15, -14) == "Las horas y el precio deben ser números positivos"
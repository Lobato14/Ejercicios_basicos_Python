from src.Ejercicio_2_7 import calculo_num

def test_calculo_num():
    assert calculo_num(3, 5, 2) == "La suma de sus números es 10"
    assert calculo_num(0, 0, 0) == "La suma de sus números es 0"
    assert calculo_num(-8, 7, 1) == "Los números introducidos no deben de ser negativos"
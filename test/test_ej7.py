from src.Ejercicio_2_7 import calculo_num

def test_calculo_num():
    assert calculo_num(3, 5, 2) == "La suma de sus números es 10"
    assert calculo_num(7, 2, 3) == "La suma de sus números es 12"
    assert calculo_num(8, 9, 1) == "La suma de sus números es 18"
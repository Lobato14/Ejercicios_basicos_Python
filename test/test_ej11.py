from src.Ejercicio_2_11 import suma_enteros

def test_suma_enteros():
    assert suma_enteros(1) == 1
    assert suma_enteros(5) == 15
    assert suma_enteros(10) == 55
    assert suma_enteros(100) == 5050
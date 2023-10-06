from src.Ejercicio_2_9 import suma_numeros

def test_suma_numeros():
    assert suma_numeros() == "La suma de sus números es de 6"
    assert suma_numeros() == "La suma de sus números es de 0"
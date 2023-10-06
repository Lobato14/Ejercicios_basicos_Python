from src.Ejercicio_2_24 import separar_euros_y_centimos

def test_separar_euros_y_centimos():
    assert separar_euros_y_centimos(3.45) == (3, 45)
    assert separar_euros_y_centimos(0.99) == (0, 99)
    assert separar_euros_y_centimos(10.00) == (10, 0)
    assert separar_euros_y_centimos(-5) == (None, None)
    assert separar_euros_y_centimos("") == (None, None)

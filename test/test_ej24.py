from src.Ejercicio_2_24 import separar_euros_y_centimos

def test_separar_euros_y_centimos():
    assert separar_euros_y_centimos("10.50") == (10, 50)
    assert separar_euros_y_centimos("123.45") == (123, 45)
    assert separar_euros_y_centimos("1.99") == (1, 99)
    assert separar_euros_y_centimos("0.01") == (0, 1)

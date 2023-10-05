from src.Ejercicio_2_20 import obtener_numero_sin_digitos

def test_obtener_numero_sin_digitos_formato_correcto():
    assert obtener_numero_sin_digitos("+34-913724710-56") == 913724710

def test_obtener_numero_sin_digitos_formato_incorrecto():
    assert obtener_numero_sin_digitos("123456") is None

def test_obtener_numero_sin_digitos_sin_prefijo():
    assert obtener_numero_sin_digitos("913724710-56") is None
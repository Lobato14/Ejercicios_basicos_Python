from Ejercicio_2_21 import fraseInvertida

def test_fraseInvertida():
    assert fraseInvertida("Hola que tal") == "tal que Hola"
    assert fraseInvertida("Tres tristes tigres") == "tigres tristes Tres"
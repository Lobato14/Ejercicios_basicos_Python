from src.Ejercicio_2_21 import fraseInvertida

def test_fraseInvertida():
    assert fraseInvertida("Hola que tal") == "tal que Hola"
    assert fraseInvertida("Tres tristes tigres") == "tigres tristes Tres"
    assert fraseInvertida(" ") == "La frase debe contener al menos dos palabras."
    assert fraseInvertida("Dos señores") == "señores Dos"
    assert fraseInvertida("señores") == "La frase debe contener al menos dos palabras."
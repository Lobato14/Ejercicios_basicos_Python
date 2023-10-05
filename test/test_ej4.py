from Ejercicio_2_4 import conversor_Celsius_Fahrenheit

# Test para números positivos
def test_conversor_Celsius_Fahrenheit_positivos():
    assert conversor_Celsius_Fahrenheit(20) == "20 grados Celsius equivale a 68.0 grados Fahrenheit"

# Test para números negativos
def test_conversor_Celsius_Fahrenheit_negativos():
    assert conversor_Celsius_Fahrenheit(-10) == "-10 grados Celsius equivale a 14.0 grados Fahrenheit"
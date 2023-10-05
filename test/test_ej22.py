from src.Ejercicio_2_22 import convertir_vocal_mayuscula

def test_convertir_vocal_mayuscula():
    assert convertir_vocal_mayuscula("Hola, este es un ejemplo de frase.", "a") == "HolA, este es un ejemplo de frAse."
    assert convertir_vocal_mayuscula("Python es un lenguaje de programacion.", "e") == "Python Es un lEnguajE dE programacion."
    assert convertir_vocal_mayuscula("La vocal es: o", "o") == "La vOcal es: O"

def test_convertir_vocal_mayuscula_sin_ocurrencias():
    assert convertir_vocal_mayuscula("Hola", "x") == "Hola"

def test_convertir_vocal_mayuscula_vacia():
    assert convertir_vocal_mayuscula("", "a") == ""
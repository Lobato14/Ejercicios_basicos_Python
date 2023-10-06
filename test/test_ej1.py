from src.Ejercicio_2_1 import obtener_saludo

def test_obtener_saludo():
    nombre = "Juan"
    nombre2 = "Paco"
    nombre3 = ""
    nombre4 = "\n"
    assert obtener_saludo(nombre) == "Hola, Juan"
    assert obtener_saludo(nombre2) == "Hola, Paco"
    assert obtener_saludo(nombre3) == "Hola, "
    assert obtener_saludo(nombre4) == "Hola, \n"
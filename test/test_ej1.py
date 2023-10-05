from src.Ejercicio_2_1 import obtener_saludo

def test_obtener_saludo():
    nombre = "Juan"
    nombre2 = "Paco"
    assert obtener_saludo(nombre) == "Hola, Juan"
    assert obtener_saludo(nombre2) == "Hola, Paco"

from Ejercicio_2_3 import resultado_parte1
from Ejercicio_2_3 import resultado_parte2
from Ejercicio_2_3 import resultado_parte3

def test_resultado_parte1():
    assert resultado_parte1(17) == "El primer resultado es 8.5"

def test_resultado_parte2():
    assert resultado_parte2(17) == "El segundo resultado es 8"

def test_resultado_parte3():
    assert resultado_parte3(12.0) == "El tercer resultado es 4.0"
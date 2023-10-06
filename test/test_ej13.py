from src.Ejercicio_2_13 import division_prog

def test_division_prog():
    assert division_prog(8, 4) == "La división de 8 entre 4 da un cociente 2 y un resto 0."
    assert division_prog(0, 0) == "La división por cero no está permitida."
    assert division_prog(-6, 3) == "La división no se puede realizar correctamente debido a números negativos."
    assert division_prog(6, -3) == "La división no se puede realizar correctamente debido a números negativos."

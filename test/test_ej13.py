from src.Ejercicio_2_13 import division_prog

def test_division_prog():
    assert division_prog(8, 4) == "La división de 8 entre 4 da un cociente 2 y un resto 0."
    assert division_prog(4, 2) == "La división de 4 entre 2 da un cociente 2 y un resto 0."
    assert division_prog(6, 3) == "La división de 6 entre 3 da un cociente 2 y un resto 0."
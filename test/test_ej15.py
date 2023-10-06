from src.Ejercicio_2_15 import cantDeposAnual

def test_cantDeposAnual():
    assert cantDeposAnual(500) == 1372.0
    assert cantDeposAnual(0) == "La cantidad depositada no puede ser 0 menor que este"
    assert cantDeposAnual(-500) == "La cantidad depositada no puede ser 0 menor que este"
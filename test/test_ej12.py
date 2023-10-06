from src.Ejercicio_2_12 import calculoIMC

def test_calculoIMC():
    assert calculoIMC(50.50, 1.70) == "Tu indice de masa corporal es de 17.47"
    assert calculoIMC(80.60, 0) == "El peso y la altura no puede ser 0 o menor que este"
    assert calculoIMC(0, 1.95) == "El peso y la altura no puede ser 0 o menor que este"
    assert calculoIMC(70.75, -1.95) == "El peso y la altura no puede ser 0 o menor que este"
    assert calculoIMC(0.0, 0.0) == "El peso y la altura no puede ser 0 o menor que este"
    assert calculoIMC(-50.50, 1.70) == "El peso y la altura no puede ser 0 o menor que este"
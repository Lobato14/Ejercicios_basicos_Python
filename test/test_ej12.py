from src.Ejercicio_2_12 import calculoIMC

def test_calculoIMC():
    assert calculoIMC(50.50, 1.70) == "Tu indice de masa corporal es de 17.47"
    assert calculoIMC(80.60, 1.85) == "Tu indice de masa corporal es de 23.55"
    assert calculoIMC(90.10, 1.95) == "Tu indice de masa corporal es de 23.69"

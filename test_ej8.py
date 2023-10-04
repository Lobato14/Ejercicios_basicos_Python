from Ejercicio_2_8 import sumar_numeros

def test_sumar_numeros():
    assert sumar_numeros([1, 2, 3]) == 6
    assert sumar_numeros([4, 5, 6]) == 15
    assert sumar_numeros([7, 8, 9]) == 24
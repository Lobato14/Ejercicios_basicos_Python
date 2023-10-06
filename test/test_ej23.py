from src.Ejercicio_2_23 import modificarEmail

def test_modificarEmail():
    assert modificarEmail("usuario@example.com") == "usuario@ceu.es"
    assert modificarEmail("correo_sin_arroba.com") == "Correo electrónico inválido. Debe contener al menos una letra y una arroba (@)."
    assert modificarEmail("123@correo_con_numero.com") == "123@ceu.es"
    assert modificarEmail("") == "Correo electrónico inválido. Debe contener al menos una letra y una arroba (@)."
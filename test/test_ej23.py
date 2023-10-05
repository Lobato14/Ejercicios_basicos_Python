from src.Ejercicio_2_23 import modificarEmail

def test_modificarEmail():
    assert modificarEmail("rubencelislobato@gmail.com") == "rubencelislobato@ceu.es"
    assert modificarEmail("nataliajimenez@gmail.com") == "nataliajimenez@ceu.es"
    assert modificarEmail("esmeraldabenitez@gmail.com") == "esmeraldabenitez@ceu.es"
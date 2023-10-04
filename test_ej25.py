from Ejercicio_2_25 import obtener_fecha_nacimiento

def test_obtener_fecha_nacimiento():
    assert obtener_fecha_nacimiento("05/5/1990") == (5, 5, 1990)
    assert obtener_fecha_nacimiento("25/12/2000") == (25, 12, 2000)
    assert obtener_fecha_nacimiento("7/03/1985") == (7, 3, 1985)
    assert obtener_fecha_nacimiento("01/1/2001") == (1, 1, 2001)

def test_obtener_fecha_nacimiento_con_un_caracter():
    assert obtener_fecha_nacimiento("1/1/2022") == (1, 1, 2022)
    assert obtener_fecha_nacimiento("15/8/1995") == (15, 8, 1995)

def test_obtener_fecha_nacimiento_con_ceros():
    assert obtener_fecha_nacimiento("05/05/1980") == (5, 5, 1980)
    assert obtener_fecha_nacimiento("01/01/2001") == (1, 1, 2001)
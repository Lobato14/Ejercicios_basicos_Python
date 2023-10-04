from Ejercicio_2_18 import procesar_nombre

def test_procesar_nombre():
    # Caso de prueba cuando el nombre completo contiene mayúsculas y minúsculas
    nombre_completo = "JoHn DoE"
    nombre_min, nombre_may, nombre_capitalizado = procesar_nombre(nombre_completo)
    assert nombre_min == "john doe"
    assert nombre_may == "JOHN DOE"
    assert nombre_capitalizado == "John Doe"

    # Caso de prueba cuando el nombre completo contiene solo minúsculas
    nombre_completo = "alice bob"
    nombre_min, nombre_may, nombre_capitalizado = procesar_nombre(nombre_completo)
    assert nombre_min == "alice bob"
    assert nombre_may == "ALICE BOB"
    assert nombre_capitalizado == "Alice Bob"

    # Caso de prueba cuando el nombre completo contiene solo mayúsculas
    nombre_completo = "CHARLIE DAVID"
    nombre_min, nombre_may, nombre_capitalizado = procesar_nombre(nombre_completo)
    assert nombre_min == "charlie david"
    assert nombre_may == "CHARLIE DAVID"
    assert nombre_capitalizado == "Charlie David"

    # Caso de prueba cuando el nombre completo está vacío
    nombre_completo = ""
    nombre_min, nombre_may, nombre_capitalizado = procesar_nombre(nombre_completo)
    assert nombre_min == ""
    assert nombre_may == ""
    assert nombre_capitalizado == ""
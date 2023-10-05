from Ejercicio_2_19 import ponerMay_NLetras

def test_ponerMay_NLetras():
    # Caso de prueba cuando el nombre es en minúsculas
    nombre = "alice"
    resultado = ponerMay_NLetras(nombre)
    assert resultado == "Nombre en mayúsculas: ALICE\nNúmero de letras: 5"
    
    # Caso de prueba cuando el nombre es en mayúsculas
    nombre = "BOB"
    resultado = ponerMay_NLetras(nombre)
    assert resultado == "Nombre en mayúsculas: BOB\nNúmero de letras: 3"
    
    # Caso de prueba cuando el nombre contiene mayúsculas y minúsculas
    nombre = "ChArLiE"
    resultado = ponerMay_NLetras(nombre)
    assert resultado == "Nombre en mayúsculas: CHARLIE\nNúmero de letras: 7"
    
    # Caso de prueba cuando el nombre está vacío
    nombre = ""
    resultado = ponerMay_NLetras(nombre)
    assert resultado == "Nombre en mayúsculas: \nNúmero de letras: 0"
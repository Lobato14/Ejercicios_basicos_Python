from src.Ejercicio_2_27 import caracteristProducto

def test_caracteristProducto_valido():
    assert caracteristProducto("Producto1", 10.5, 3) == 31.5
    assert caracteristProducto("Producto2", 5.2, 2) == 10.4
    assert caracteristProducto("Producto3", 8.0, 5) == 40.0

def test_caracteristProducto_invalido():
    assert caracteristProducto("Producto4", 10.0, 0) == "La operación no es válida porque has escrito números negativos"
    assert caracteristProducto("Producto5", 20.0, -1) == "La operación no es válida porque has escrito números negativos"
from src.Ejercicio_2_26 import mostrar_lista_compra

def test_mostrar_lista_compra():
    assert mostrar_lista_compra("manzanas, peras, plátanos") == "manzanas\nperas\nplátanos\n"
    assert mostrar_lista_compra("leche") == "Error: La lista de compra está vacía o no contiene productos separados por comas."
    assert mostrar_lista_compra("") == "Error: La lista de compra está vacía o no contiene productos separados por comas."
    assert mostrar_lista_compra("manzanas;peras;plátanos") == "Error: La lista de compra está vacía o no contiene productos separados por comas."
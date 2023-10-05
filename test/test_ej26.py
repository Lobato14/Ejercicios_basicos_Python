from Ejercicio_2_26 import mostrar_lista_compra

def test_mostrar_lista_compra():
    assert mostrar_lista_compra("huevos, platanos, manzanas") == "huevos\nplatanos\nmanzanas\n"
    assert mostrar_lista_compra("sardinas, mangos , zumo, coca-cola") == "sardinas\nmangos\nzumo\ncoca-cola\n"
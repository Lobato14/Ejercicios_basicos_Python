from src.Ejercicio_2_17 import nombreVeces
import pytest
@pytest.mark.parametrize(
    "input_nombre, input_numero, expected_output",
    [
        ("Alice", 0, ""),
        ("Bob", 1, "Bob\n"),
        ("Charlie", 3, "Charlie\nCharlie\nCharlie\n"),
        ("", 5, ""),
        ("Dave", -2, "")
    ]
)
def test_nombreVeces(input_nombre, input_numero, expected_output):
    assert nombreVeces(input_nombre, input_numero) == expected_output
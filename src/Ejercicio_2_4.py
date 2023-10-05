# Escribe un programa que le pida al usuario una temperatura en grados Celsius,
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

def conversor_Celsius_Fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius} grados Celsius equivale a {fahrenheit} grados Fahrenheit"

if __name__ == "__main__":
    celsius = float(input("Escriba la temperatura en grados Celsius: "))
    resultado = conversor_Celsius_Fahrenheit(celsius)
    print(resultado)
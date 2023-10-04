# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre
# combinando mayúsculas y minúsculas como quiera.

def procesar_nombre(nombre_completo):
    # Con lower muestra el nombre en minúsculas
    nombre_min = nombre_completo.lower()
    # Con upper muestra el nombre en mayúsculas
    nombre_may = nombre_completo.upper()
    # Con split dividimos cada palabra de la frase introducida
    palabras = nombre_completo.split()
    # Con join unimos las palabras y con capitalize convertimos la primera palabra de una cadena en mayúsculas
    nombre_capitalizado = ' '.join([palabra.capitalize() for palabra in palabras])
    return nombre_min, nombre_may, nombre_capitalizado

if __name__ == "__main__":
    nombre_completo = input("Escriba su nombre completo: ")
    nombre_min, nombre_may, nombre_capitalizado = procesar_nombre(nombre_completo)
    print("Nombre en minúsculas: ", nombre_min)
    print("Nombre en mayúsculas: ", nombre_may)
    print("Nombre capitalizado: ", nombre_capitalizado)

# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida .

def obtener_saludo(nombre):
    return "Hola, " + nombre

if __name__=="__main__":
    nombre = input("Escribe tu nombre: ")
    print(obtener_saludo(nombre))
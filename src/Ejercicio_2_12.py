# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y
# lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa
# corporal calculado redondeado con dos decimales.

def calculoIMC(peso, altura):
    if peso <= 0 or altura <= 0:
        return "El peso y la altura no puede ser 0 o menor que este"
    IMC = peso / (altura)**2
    IMC_redondeado = round(IMC, 2)
    return "Tu indice de masa corporal es de " + str(IMC_redondeado)

if __name__=="__main__":
    peso = float(input("Escriba su peso: "))
    altura = float(input("Escriba su altura: "))
    print(calculoIMC(peso, altura))
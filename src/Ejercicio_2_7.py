# Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def calculo_num(numero1, numero2, numero3):
    if numero1 < 0 or numero2 < 0 or numero3 < 0:
        return "Los números introducidos no deben de ser negativos"
    suma = numero1 + numero2 + numero3
    return "La suma de sus números es " + str(suma)

if __name__=="__main__":
    numero1 = int(input("Escribe un numero: "))
    numero2 = int(input("Escribe un numero: "))
    numero3 = int(input("Escribe un numero: "))
    print(calculo_num(numero1, numero2, numero3))
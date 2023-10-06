# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo
# electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def modificarEmail(email):
    # Verificar si la cadena contiene al menos una letra y una arroba (@)
    if any(c.isalpha() for c in email) and "@" in email:
        # Dividimos el correo en dos partes: nombre y dominio con split
        nombre, dominio = email.split("@")
        emailMod = nombre + "@ceu.es"
        return emailMod
    else:
        return "Correo electrónico inválido. Debe contener al menos una letra y una arroba (@)."

if __name__ == "__main__":
    email = input("Escriba su correo electronico: ")
    texto = modificarEmail(email)
    print("Tu correo es ", texto)
def mostrar_formulario():
    print("===== Formulario de Login =====")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    procesar_login(email, password)

def es_correo_valido(correo):
    # Verifica que el correo contenga "@" y "."
    return "@" in correo and "." in correo

def procesar_login(email, password):
    if es_correo_valido(email):
        print(f"Inicio de sesión exitoso. Bienvenido, {email}!")
    else:
        print("Inicio de sesión fallido. Por favor, ingresa un correo electrónico válido.")

# Simulación del programa
if __name__ == "__main__":
    mostrar_formulario()

def actualizar_intentos(letra, palabra, intentos_restantes):
    if letra.lower() not in palabra.lower():
        intentos_restantes -= 1
        print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
    else:
        print("¡Buen trabajo! Has adivinado una letra.")
    return intentos_restantes

# Ejemplo de uso
palabra = 'python'
intentos_restantes = 5
letra = 'x'
intentos_restantes = actualizar_intentos(letra, palabra, intentos_restantes)

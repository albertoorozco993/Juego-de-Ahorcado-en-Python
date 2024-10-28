import random

def mostrar_palabra(palabra, letras_adivinadas):
    estado = ''
    for letra in palabra:
        if letra.lower() in letras_adivinadas:
            estado += letra + ' '
        else:
            estado += '_ '
    return estado.strip()

def actualizar_intentos(letra, palabra, intentos_restantes):
    if letra.lower() not in palabra.lower():
        intentos_restantes -= 1
        print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
    else:
        print("¡Buen trabajo! Has adivinado una letra.")
    return intentos_restantes

def verificar_ganador(palabra, letras_adivinadas):
    for letra in palabra.lower():
        if letra not in letras_adivinadas:
            return False
    return True

def pedir_letra(letras_ingresadas):
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Debes ingresar una sola letra.")
        elif letra in letras_ingresadas:
            print("Ya has ingresado esa letra. Intenta con otra.")
        else:
            letras_ingresadas.add(letra)
            return letra

def jugar():
    palabras = ['python', 'programacion', 'innovacion', 'tecnologia', 'ahorcado']
    palabra = random.choice(palabras)
    letras_adivinadas = set()
    letras_ingresadas = set()
    intentos_restantes = 10

    while intentos_restantes > 0:
        print("\n" + mostrar_palabra(palabra, letras_adivinadas))
        letra = pedir_letra(letras_ingresadas)
        letras_adivinadas.add(letra)
        intentos_restantes = actualizar_intentos(letra, palabra, intentos_restantes)

        if verificar_ganador(palabra, letras_adivinadas):
            print(f"¡Has ganado! La palabra era '{palabra}'.")
            break
    else:
        print(f"Has perdido. La palabra era '{palabra}'.")

# Iniciar el juego
jugar()

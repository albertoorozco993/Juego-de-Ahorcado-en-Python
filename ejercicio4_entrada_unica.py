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

# Ejemplo de uso
letras_ingresadas = set()
letra = pedir_letra(letras_ingresadas)

def mostrar_palabra(palabra, letras_adivinadas):
    estado = ''
    for letra in palabra:
        if letra.lower() in letras_adivinadas:
            estado += letra + ' '
        else:
            estado += '_ '
    return estado.strip()

# Ejemplo de uso
palabra = 'programacion'
letras_adivinadas = {'p', 'r', 'o'}
print(mostrar_palabra(palabra, letras_adivinadas))

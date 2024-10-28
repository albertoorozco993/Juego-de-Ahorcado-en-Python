def verificar_ganador(palabra, letras_adivinadas):
    for letra in palabra.lower():
        if letra not in letras_adivinadas:
            return False
    return True

# Ejemplo de uso
palabra = 'data'
letras_adivinadas = {'d', 'a', 't'}
if verificar_ganador(palabra, letras_adivinadas):
    print("¡Felicidades, has ganado!")
else:
    print("Continúa jugando.")

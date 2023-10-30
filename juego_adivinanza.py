import random
def juego_adivinanza():
    """Este funcion lo que hará es crear un juego de adivinanza de verdadero y falso"""
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    print("¡Bienvenido al juego de adivinanza!")
    print(f"Adivina el número entre 1 y 100. Tienes un máximo de {max_intentos} intentos.")
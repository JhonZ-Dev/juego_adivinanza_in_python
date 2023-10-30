import random
def juego_adivinanza():
    """Este funcion lo que hará es crear un juego de adivinanza de verdadero y falso"""
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
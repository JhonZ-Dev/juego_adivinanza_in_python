import random
def juego_adivinanza():
    """Este funcion lo que hará es crear un juego de adivinanza de verdadero y falso"""
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    print("¡Bienvenido al juego de adivinanza!")
    print(f"Adivina el número entre 1 y 100. Tienes un máximo de {max_intentos} intentos.")
    while intentos < max_intentos:
        intento = int(input("Introduce tu suposición: "))

        if intento < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número secreto ({numero_secreto}) en {intentos + 1} intentos!")
            break

        intentos += 1
    if intentos == max_intentos:
        print(f"¡Agotaste tus {max_intentos} intentos! El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")
if __name__ == "__main__":
    juego_adivinanza()
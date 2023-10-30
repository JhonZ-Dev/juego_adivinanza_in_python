import random
def juego_adivinanza():
    """Este funcion lo que hará es crear un juego de adivinanza de verdadero y falso"""
 

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
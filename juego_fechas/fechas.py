import random
import sys
from preguntas_fechas import preguntas


def jugar():
    pregunta = random.choice(preguntas)
    respuesta_correcta = pregunta["respuesta"]
    respuesta_usuario = input(pregunta["pregunta"] + "\n")

    if respuesta_correcta == respuesta_usuario:
        print("¡Has acertado!")
    else:
        print("Has fallado, es ", respuesta_correcta)

    continuar()


def continuar():
    continuacion = input("¿Quieres seguir jugando? (s/n) ")

    while continuacion.lower() not in ["s", "n"]:
        print("Entrada no válida. Introduce 's' o 'n'.")
        continuar()

    if continuacion.lower() == "s":
        jugar()
    else:
        print("¡Hasta luego!")
        sys.exit()


print("Hola, ¡vamos a aprender fechas!")
jugar()

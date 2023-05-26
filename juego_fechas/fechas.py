import random
import sys
from preguntas_fechas import preguntas

aciertos = 0
fallos = 0


def jugar():
    global aciertos
    global fallos

    pregunta = random.choice(preguntas)
    respuesta_correcta = pregunta["respuesta"]
    respuesta_usuario = input(pregunta["pregunta"] + "\n")

    if respuesta_correcta == respuesta_usuario:
        print("¡Has acertado!")
        aciertos += 1
    else:
        print("Has fallado, es ", respuesta_correcta)
        fallos += 1

    continuar()


def continuar():
    continuacion = input("¿Quieres seguir jugando? (s/n) ")

    while continuacion.lower() not in ["s", "n"]:
        print("Entrada no válida. Introduce 's' o 'n'.")
        continuar()

    if continuacion.lower() == "s":
        jugar()
    else:
        print("Has tenido ", aciertos, " aciertos, ", fallos, " fallos")
        print("¡Hasta luego!")
        sys.exit()


print("Hola ¡¿cómo están los máquinas?!")
jugar()

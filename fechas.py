import random
from preguntas_fechas import preguntas


def jugar():
    pregunta = random.choice(preguntas)
    respuesta_correcta = pregunta["respuesta"]
    respuesta_usuario = input(pregunta["pregunta"] + "\n")

    if respuesta_correcta == respuesta_usuario:
        print("¡Has acertado!")
    else:
        print("Has fallado, es ", respuesta_correcta)

    continuacion = input("¿Quieres seguir jugando? (s/n) ")
    if continuacion == "s":
        jugar()
    elif continuacion == "n":
        print("¡Hasta luego!")
    else:
        print("Entrada no válida. Introduce 's' o 'n'.")
        continuacion = input("¿Quieres seguir jugando? (s/n) ")


print("Hola, ¡vamos a aprender fechas!")
jugar()

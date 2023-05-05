import random

preguntas = [
    {
        "pregunta": "¿En qué año se firmó la paz de Westfalia?",
        "respuesta": "1648"
    },
    {
        "pregunta": "¿En qué año finalizó el reinado de Carlos II?",
        "respuesta": "1700"
    }
]


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
        jugar()


print("Hola, ¡vamos a aprender fechas!")
jugar()

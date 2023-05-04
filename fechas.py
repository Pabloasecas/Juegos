import random
print("Hola, ¡vamos a aprender fechas!")
# paz_de_westfalia = "La Paz de Westfalia"
# respuesta_correcta = int(1648)
# print("En qué año se produjo", paz_de_westfalia)
# respuesta_usuario = int(input())
preguntas = [
    {
        "pregunta": "¿En qué año se firmó la paz de Westfalia?",
        "respuesta": "1648"
    },
]


def pregunta_aleatoria(preguntas):
    pregunta = random.choice(preguntas)
    respuesta_usuario = input(pregunta["pregunta"] + "\n")
    restpuesta_correcta = pregunta["respuesta"]
    return respuesta_usuario, restpuesta_correcta


def juego(respuesta_correcta, respuesta_usuario):
    if respuesta_correcta == respuesta_usuario:
        print("¡Has acertado!")
    else:
        print("Has fallado, fue en", respuesta_correcta)
    return juego

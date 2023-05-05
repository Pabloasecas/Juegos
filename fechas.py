import random
print("Hola, ¡vamos a aprender fechas!")
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

pregunta = random.choice(preguntas)
respuesta_usuario = input(pregunta["pregunta"] + "\n")
respuesta_correcta = pregunta["respuesta"]

if respuesta_correcta == respuesta_usuario:
    print("¡Has acertado!")
else:
    print("Has fallado")
continuacion = input("¿Quieres seguir jugando? (s/n) ")
if continuacion == "s":
    valor_continuacion = True
elif continuacion == "n":
    valor_continuacion = False
else:
    print("Entrada no válida. Introduce 's' o 'n'.")
while valor_continuacion == True:
    pregunta = random.choice(preguntas)
    respuesta_usuario = input(pregunta["pregunta"] + "\n")
    respuesta_correcta = pregunta["respuesta"]
    continuacion = input("¿Quieres seguir jugando? (s/n) ")
    if continuacion == "s":
        valor_continuacion = True
    elif continuacion == "n":
        valor_continuacion = False
    else:
        print("Entrada no válida. Introduce 's' o 'n'.")

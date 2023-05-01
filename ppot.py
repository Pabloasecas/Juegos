import random

print("Hola, juguemos a Piedra, papel o tijera")
print("Piedra, Papel o Tijera...")
PIEDRA = "piedra"
PAPEL = "papel"
TIJERA = "tijera"
elemento_programa = [PIEDRA, PAPEL, TIJERA][random.randint(0, 2)]
elemento_usuario = input()
print(elemento_programa)

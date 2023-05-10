import random

print("Hola, juguemos a Piedra, papel o tijera")
print("Piedra, Papel o Tijera...")
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERA = "Tijera"
elemento_programa = [PIEDRA, PAPEL, TIJERA][random.randint(0, 2)]
elemento_usuario = input()
print(elemento_programa)

while elemento_programa == elemento_usuario:
    print("Piedra, Papel o Tijera...")
    elemento_programa = [PIEDRA, PAPEL, TIJERA][random.randint(0, 2)]
    elemento_usuario = input()
    print(elemento_programa)

if elemento_programa == PAPEL:
    if elemento_usuario == PIEDRA:
        print("¡He ganado!")
    else:
        print("¡Has ganado!")

elif elemento_programa == PIEDRA:
    if elemento_usuario == TIJERA:
        print("¡He ganado!")
    else:
        print("¡Has ganado!")

else:
    if elemento_usuario == PAPEL:
        print("¡He ganado!")
    else:
        print("¡Has ganado!")

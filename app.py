#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# Select a random element from a list
from random import choice
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

puntuacion = 0
jugar = True
opciones = ["piedra", "papel", "tijeras"]
while jugar:
    valido = False
    while not valido:
        jugador = input("Piedra, papel o tijeras: ").lower()
        if jugador not in opciones:
            print("Opción inválida")
            continue
        valido = True
    computadora = choice(opciones)
    if jugador == computadora:
        print("Empate")
    elif jugador == "piedra" and computadora == "tijeras":
        print("Ganaste")
        puntuacion += 1
    elif jugador == "papel" and computadora == "piedra":
        print("Ganaste")
        puntuacion += 1
    elif jugador == "tijeras" and computadora == "papel":
        print("Ganaste")
        puntuacion += 1
    else:
        print("Perdiste")
    again = input("¿Jugar de nuevo? (s/n): ").lower()
    if again == "n":
        jugar = False
        print("Tu puntuación final es: " + str(puntuacion) + " puntos")


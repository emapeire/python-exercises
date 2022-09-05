import random
import string

from palabras import palabras
from ahorcado_diagramas import *

def obtener_palabras(palabras):
    # Seleccionar una palabra aleatoria de la lista de palabras válidas.
    palabra = random.choice(palabras)
    
    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()


def ahorcado():
    
    print("\n=================================================")
    print("     ¡Bienvenido/a al juego del ahorcado!     ")
    print("=================================================\n")
    print("Tu meta es adivinar todas las letras de una palabra aleatoria sin morir en el intento.")
    print("¡Vamos a por ello!\n")
    
    palabra = obtener_palabras(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() # Una lista de letras que ya se han adivinado.
    abecedario = set(string.ascii_uppercase) # No está la ñ
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Mostrar el estado actual de la palabra.
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        # Mostrar estado del ahorcado.
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio.
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escribe una letra: ").upper()
        
        # Si la letra elegida por el usuario está en el abecedario y no en la lista de letras adivinadas,
        # se añade a la lista de letras adivinadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
        
ahorcado()
import random

def adivina_el_numero_computadora():
    print("\n=======================================")
    print("        ¡Bienvenido/a al juego!        ")
    print("=======================================\n")
    print("¡Hola humano/a! Soy tu computadora personal.")
    print("Intentaré adivinar un número entre 1 y el que tú dispongas.\n")
    
    limite_superior = int(input("Indica el número del límite superior para establecer un rango (por ejemplo el 10): "))
    limite_inferior = 1
    
    print(f"\n¡Excelente! El número que intentaré adivinar estará entre 1 y {limite_superior}.")

    while True:
        prediccion = random.randint(limite_inferior, limite_superior)
        respuesta = input(f"\nMi predicción es {prediccion}. ¿Es el número correcto? (Si/No): ").lower()

        if respuesta == "si":
            print("\n¡Excelente! He acertado.")
            break
        elif respuesta == "no":
            direccion = input(f"\n¿El número que piensas es más alto o más bajo que {prediccion}? Más alto (A) / Más bajo (B): ").lower()
            if direccion == "a":
                limite_inferior = prediccion + 1
            elif direccion == "b":
                limite_superior = prediccion - 1
            else:
                print("\n¡No has introducido una respuesta válida!")
        else:
            print("\n¡No has introducido una respuesta válida!")
    
    jugar_otra_vez = input(f"\n¿Quieres volver a jugar? (Si/No): ").lower()
    if jugar_otra_vez == "si":
        adivina_el_numero_computadora()

adivina_el_numero_computadora()

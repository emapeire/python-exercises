import random

limite_superior = ""

def adivina_el_numero_computadora(x):
    
    print("\n=======================================")
    print("        ¡Bienvenido/a al juego!        ")
    print("=======================================\n")
    print("¡Hola humano/a! Soy tu computadora personal.")
    print("Intentaré adivinarte un número entre 1 y el que tú dispongas.\n")
    
    x = int(input("Indica el número del límite superior para establecer un rango (por ejemplo el 10): "))
    limite_inferior = 1
    global limite_superior
    limite_superior = x
    
    print(f"\n¡Excelente! El número que intentaré adivinar estará entre 1 y {x}.")
    
    listo = input(f"\n¿Estas listo/a para jugar? (Si/No): ").lower()
    if listo == "si" or listo == "s":
        
        respuesta = ""
        while respuesta != "si" or respuesta != "s":
            # Generar predicción
            if limite_inferior != limite_superior:
                prediccion = random.randint(limite_inferior, limite_superior)
            else: # Si el limite_inferior y el limite_superior son iguales, la prediccion es el limite_inferior.
                prediccion = limite_inferior
        
            # Obtener respuesta del usuario
            respuesta = input(f"\nMi predicción es {prediccion}. ¿Es el número correcto? (Si/No): ").lower()

            if respuesta == "no" or respuesta == "n":
                respuesta = input(f"\n¿El número que piensas es más alto o más bajo que {prediccion}? Más alto (A) / Más bajo (B): ").lower()
            
                if respuesta == "a":
                    # prediccion = random.randint(prediccion + 1, limite_superior)
                    # return prediccion
                    limite_inferior = prediccion + 1
        
                elif respuesta == "b":
                    # prediccion = random.randint(limite_inferior, prediccion - 1)
                    # return prediccion
                    limite_superior = prediccion - 1
                
                else:
                    print("\n¡No has introducido una respuesta válida!")
        
            elif respuesta == "si" or respuesta == "s":
                print("\n¡Excelente! He acertado.")
                respuesta = input(f"\n¿Quieres volver a jugar? (Si/No): ").lower()
                
                if respuesta == "si" or respuesta == "s":
                    adivina_el_numero_computadora(x)
                
                elif respuesta == "no" or respuesta == "n":
                    print("\n¡Hasta luego!\n")
                    return exit()
            
            else:
                print("\n¡No has introducido una respuesta válida!")
    
    elif listo == "no" or listo == "n":
        respuesta = (input(f"\n¿Queres volver a intentarlo? (Si/No): ").lower())
        
        if respuesta == "si" or respuesta == "s":
            adivina_el_numero_computadora(x)
        
        elif respuesta == "no" or respuesta == "n":
            print("\n¡Hasta luego!\n")
            return exit()
        

adivina_el_numero_computadora(limite_superior)
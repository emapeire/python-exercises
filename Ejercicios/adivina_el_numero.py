import random
# import this
# print(this)

input_numero = ""

def adivina_el_numero(x):
    
    print("\n=======================================")
    print("        ¡Bienvenido/a al juego!        ")
    print("=======================================\n")
    print("Tu meta es adivinar el número generado por la computadora.")
    print("¡Vamos a por ello!\n")
    
    global input_numero
    input_numero = input("Ingresa un número entre 1 y cualquier otro: ")
    x = int(input_numero)
    
    numero_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x.
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        # El usuario ingresa un número.    
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) # f-string
        
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. El número que ingresaste es muy bajo.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. El número que ingresaste es muy alto.")
    
    print("")
    print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(input_numero)
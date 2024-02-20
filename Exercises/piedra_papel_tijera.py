import random


def jugar():
    
    print("\n=======================================")
    print("        ¡Bienvenido/a al juego!        ")
    print("=======================================\n")
    print("Vamos a jugar: '¿Piedra, papel o tijera?'\n")
    
    usuario = input("Elige una opción: Piedra (pi), Papel (pa) o Tijera (ti).\n\n").lower()
    computadora = random.choice(["pi", "pa", "ti"])

    if usuario == computadora:
        print(f"\nLa computadora eligió {computadora}.")
        print("\n¡Empate!\n")
        return de_nuevo()
        
    if gana_el_jugador(usuario, computadora):
        print(f"\nLa computadora eligió {computadora}.")
        print("\n¡Ganaste!\n")
        return de_nuevo()

    else:
        print(f"\nLa computadora eligió {computadora}.")
        print("\n¡Perdiste!\n")
        return de_nuevo()


def gana_el_jugador(jugador, oponente):
    
    # Retornar True si gana el jugador.
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).

    if((jugador == "pi" and oponente == "ti")
       or (jugador == "ti" and oponente == "pa")
       or (jugador == "pa" and oponente == "pi")):
        return True
    else:
        return False


def de_nuevo():
    
    de_nuevo = input("¿Quieres jugar de nuevo? (s/n)\n\n").lower()
    
    if de_nuevo == "s":
        return jugar()
    
    else:
        print("\n¡Hasta luego!\n")
        return exit()


print(jugar())
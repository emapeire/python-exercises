# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con _______________________.

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + str(organizacion))
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") # f-string

# Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo plural: ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}."

print(madlib)
with open ("frase.txt", mode="r") as archivo:
    for linea in archivo:
        print("==== FRASE ====")
        print(linea)

###############################################

notas = {
    "Nora": 87,
    "Gino": 100,
    "Lorenzo": 67,
    "Talia": 45
}

with open("data_estudiantes.txt", mode="w+") as archivo_notas:
    for nombre, nota in notas.items():
        archivo_notas.write(nombre + " - " + str(nota) + "\n")
        print(nombre, nota)

###############################################

nuevas_notas = {
    "Emily": 54,
    "Daniel": 98,
    "Julia": 78
}

with open("data_estudiantes.txt", mode="a+") as archivo_notas:
    for nombre, nota in nuevas_notas.items():
        archivo_notas.write(nombre + " -  " + str(nota) + "\n")
        print(nombre, nota)


# Ciclo "for"
print("Ciclo for")

# variable "letras"
letras = {"a": 1, "b": 2}

for clave in letras:
    print(clave)

for valor in letras.values():
    print(valor)

for clave, valor in letras.items():
    print(clave, valor)

# Ciclo "while"
print("Ciclo while")

# variable "x"
x = 20

while x <= 35:
    print(x)
    x += 3

# Funciones
print("Funciones")

# 1
def mostrar_doble(num):
    print(num * 2)

mostrar_doble(4)

# 2
def sumar(x, y):
    return x + y

resultado_suma = sumar(2, 2)
print(resultado_suma)

# 3
def restar(x, y):
    print(x - y)
    return x - y

resultado_resta = restar(4, 2)
print(resultado_resta)

# 4
x = 6

def f(y):
    global x
    print(x + y)

f(2)

# 5
sumar = 1

def sumar_de():
    global sumar
    sumar += 1

sumar_de()
print(sumar)

# 7
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

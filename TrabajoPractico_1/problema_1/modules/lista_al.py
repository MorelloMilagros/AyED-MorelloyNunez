import random

def generar_lista_aleatoria():
    cant_numeros = random.randint(500, 1000)  # Generar un número aleatorio entre 500 y 1000
    lista = [random.randint(10000, 99999) for _ in range(cant_numeros)]
    return lista

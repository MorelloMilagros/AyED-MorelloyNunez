import random

def generar_lista_aleatoria():
    cant_numeros = random.randint(1, 100)  # Cantidad aleatoria de números en la lista
    lista = [random.randint(0, 500) for _ in range(cant_numeros)]
    return lista

def obtener_tamaño_de_lista(lista):
    n = len(lista)
    return n
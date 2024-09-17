import time
import random
import matplotlib.pyplot as plt
from algoritmos import ord_burbuja, quicksort, radix_sort

# Funciones de ordenamiento ya definidas (ord_burbuja, quicksort, radix_sort)

# Función para medir el tiempo de ejecución de cada algoritmo
def medir_tiempos():
    tamaños = range(1, 1001)
    tiempos_burbuja = []
    tiempos_quicksort = []
    tiempos_radix = []
    tiempos_sorted = []

    for tamaño in tamaños:
        lista = [random.randint(10000, 99999) for _ in range(tamaño)]

        # Medir tiempo para burbuja
        inicio = time.time()
        ord_burbuja(lista.copy())
        tiempos_burbuja.append(time.time() - inicio)

        # Medir tiempo para quicksort
        inicio = time.time()
        quicksort(lista.copy())
        tiempos_quicksort.append(time.time() - inicio)

        # Medir tiempo para radix sort
        inicio = time.time()
        radix_sort(lista.copy())
        tiempos_radix.append(time.time() - inicio)

        # Medir tiempo para sorted
        inicio = time.time()
        sorted(lista.copy())
        tiempos_sorted.append(time.time() - inicio)

    # Graficar los tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_burbuja, label='Burbuja')
    plt.plot(tamaños, tiempos_quicksort, label='Quicksort')
    plt.plot(tamaños, tiempos_radix, label='Radix Sort')
    plt.plot(tamaños, tiempos_sorted, label='sorted')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend()
    plt.show()

# Llamar a la función para medir y graficar
medir_tiempos()
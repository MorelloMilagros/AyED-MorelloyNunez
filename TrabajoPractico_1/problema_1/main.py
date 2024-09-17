from modules.algoritmos import ord_burbuja, quicksort, radix_sort
from modules.lista_al import generar_lista_aleatoria

#Se generan listas aleatorias con otra funcion

lista = generar_lista_aleatoria()

print("Lista original: ", lista)

#Se ordena con el algoritmo de burbuja.

lista_b = lista.copy()
lista_b = ord_burbuja(lista_b)

print(lista_b)

#Se ordena con el algoritmo quicksort.

lista_q = lista.copy()
lista_q = quicksort(lista_q)

print(lista_q)

#Se ordena con el algoritmo radixsort.

lista_r = lista.copy()
lista_r = radix_sort(lista_r)

print(lista_r)
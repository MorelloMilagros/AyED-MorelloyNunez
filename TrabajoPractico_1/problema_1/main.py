from modules.algoritmos import ord_burbuja, quicksort
from modules.lista_al import generar_lista_aleatoria

#Se generan listas aleatorias con otra funcion

lista_b = generar_lista_aleatoria()
lista_q = generar_lista_aleatoria()
lista_r = generar_lista_aleatoria()

print("Lista burbuja: ", lista_b)
print("Lista quicksort: ", lista_q)
#print("Lista radix: ", lista_r)

#Se ordena con el algoritmo de burbuja.
lista_b = ord_burbuja(lista_b)

print(lista_b)

#Se ordena con el algoritmo quicksort.

lista_q = quicksort(lista_q)

print(lista_q)

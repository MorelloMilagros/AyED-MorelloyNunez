# Aqui se hubicaran los algoritmos de ordenamiento, que luego seran implementados en el main

#Algoritmo de burbuja
def ord_burbuja(lista):
    n = len(lista)
    for i in range(n-1):       # Aqui se comiena el bucle que hace que la lista se recorra cada vez
        for j in range(n-1-i): # Aqui se encuentra el bucle que recorre cada elemento de la lista
            if lista[j] > lista[j+1]:  # Verifica si el elemento a la izquierda es mayor que el de la derecha
                lista[j], lista[j+1] = lista[j+1], lista[j]   #En caso de serlo los intercambia y sigue con el siguiente par de elementos
    return lista

# Algoritmo Quicksort
def quicksort(lista2):
    if len(lista2) <= 1:  # Se verifica si la lista tiene solo un elemento, 
                          # en dicho caso la misma ya se encuentra ordenada y solo muestra la misma
        return lista2
    
    pivote = lista2[len(lista2) // 2]  # Se sellecciona un pivote del medio de la lista
    menores = [x for x in lista2 if x < pivote] # Se realiza una sublista con los elementos menores que el pivote
    pivotes = [x for x in lista2 if x == pivote]  # La lista con el pivote y los elementos iguales que el mismo
    mayores = [x for x in lista2 if x > pivote]   # Se realiza una sublista con los elementos mayores que el pivote
    
    return quicksort(menores) + pivotes + quicksort(mayores) # Aqui se realiza una llamada recursiva a la misma funcion
                                                             # de manera que se realiza el proceso anterior una y otra vez 
                                                             # con las sublistas hasta que las mismas esten ordenadas, 
                                                             # eligiendo nuevos pivotes y repitiendo el camino las veces necesarias
# Algoritmo Radixsort

def radix_sort(lista):
    # Encontrar el número más grande para saber el número de dígitos
    max_num = max(lista)
    exp = 1  # Comienza con el dígito menos significativo

    # Continuar hasta que pasemos por todos los dígitos del número más grande
    while max_num // exp > 0:
        # Crear listas de buckets para cada dígito (0 a 9)
        buckets = [[] for _ in range(10)]

        # Colocar los elementos en los buckets según el dígito actual
        for num in lista:
            index = (num // exp) % 10
            buckets[index].append(num)

        # Combinar todos los buckets en una lista ordenada
        lista = [num for bucket in buckets for num in bucket]

        # Mover al siguiente dígito
        exp *= 10

    return lista
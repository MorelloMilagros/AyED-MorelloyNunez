from modules_op2.prim import leer_archivo, mostrar_resultados, prim
archivo = "data/aldeas.txt"
grafo = leer_archivo(archivo)

# Encontrar el vértice de inicio, en este caso "Peligros"
inicio = grafo.obtener_vertice("Peligros")
if not inicio:
    raise Exception("No se encontró la aldea inicial 'Peligros' en el archivo.")

# Ejecutar el algoritmo de Prim
prim(grafo, inicio)

# Mostrar resultados
mostrar_resultados(grafo)
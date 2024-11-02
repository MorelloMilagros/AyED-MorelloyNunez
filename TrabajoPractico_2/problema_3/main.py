from modules.prim import prim
from modules.funciones import cargar_grafo_desde_archivo, mostrar_resultados

archivo = "data/aldeas.txt"
grafo = cargar_grafo_desde_archivo(archivo)
arbol_mst = prim(grafo, grafo.obtener_vertice("Peligros"))

# Mostrar resultados
mostrar_resultados(grafo)
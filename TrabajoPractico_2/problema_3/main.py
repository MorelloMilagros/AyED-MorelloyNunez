from modules.prim import prim
from modules.funciones import cargar_grafo_desde_archivo, mostrar_resultados, dibujar_mst_desde_prim, dibujar_grafo_original

archivo = "data/aldeas.txt"
grafo = cargar_grafo_desde_archivo(archivo)
arbol_mst = prim(grafo, grafo.obtener_vertice("Peligros"))

# Mostrar resultados
mostrar_resultados(arbol_mst)

#Dibujar el arbol
dibujar_mst_desde_prim(grafo)

#Graficar el grafo original
dibujar_grafo_original(grafo)
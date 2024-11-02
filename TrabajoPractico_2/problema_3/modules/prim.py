from modules.cola import ColaPrioridad
import sys

def prim(G, inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    cp.construir_monticulo([(v.obtener_distancia(), v) for v in G])

    while not cp.esta_vacia():
        vertice_actual = cp.eliminar_min()[1]  # Solo extraemos el vértice del mínimo
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vertice_siguiente)
            if cp.contiene(vertice_siguiente) and nuevo_costo < vertice_siguiente.obtener_distancia():
                vertice_siguiente.asignar_predecesor(vertice_actual)
                vertice_siguiente.asignar_distancia(nuevo_costo)
                cp.decrementar_clave(vertice_siguiente, nuevo_costo)
    return G





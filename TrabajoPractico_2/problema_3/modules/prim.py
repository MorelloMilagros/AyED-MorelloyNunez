from modules.clases import ArbolMST
from modules.cola import ColaPrioridad

def prim(grafo, inicio_id):
    # Crear el montículo de prioridad
    cp = ColaPrioridad()
    
    # Inicializar las distancias de todos los vértices a infinito
    for vertice in grafo:
        vertice.asignar_distancia(float('inf'))
        vertice.asignar_predecesor(None)
    
    # Configura la distancia del nodo inicial a 0 y agrega al montículo
    inicio = grafo.obtener_vertice(inicio_id)
    inicio.asignar_distancia(0)
    cp.construirMonticulo([(vertice.obtener_distancia(), vertice) for vertice in grafo])
    
    visitados = set()  # Llevar un registro de los nodos visitados

    while not cp.estaVacia():
        # Eliminar el vértice con la distancia mínima desde el montículo
        distancia_actual, vertice_actual = cp.eliminarMin()
        
        # Si el vértice actual ya fue visitado, lo omitimos
        if vertice_actual in visitados:
            continue
        
        visitados.add(vertice_actual)
        print(f"Seleccionado: {vertice_actual.obtener_id()} con distancia {distancia_actual}")
        
        # Iterar sobre los vecinos del vértice actual
        for vecino in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vecino)
            
            # Solo procesar si el vecino no ha sido visitado y el nuevo costo es menor
            if vecino not in visitados and nuevo_costo < vecino.obtener_distancia():
                vecino.asignar_predecesor(vertice_actual)
                vecino.asignar_distancia(nuevo_costo)
                
                # Actualizar el vecino en el montículo de prioridad
                cp.decrementarClave(vecino, nuevo_costo)
                print(f"Actualizado: {vecino.obtener_id()} con nuevo costo {nuevo_costo}")

    # Construcción del MST
    arbol_mst = ArbolMST()
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor:
            distancia = vertice.obtener_distancia()
            arbol_mst.agregar_conexion(predecesor.obtener_id(), vertice.obtener_id(), distancia)

    print(f"Suma total del MST generado: {arbol_mst.total_distancia}")
    
    return arbol_mst




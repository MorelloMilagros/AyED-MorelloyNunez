from modules_op2.monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()  # Utiliza MonticuloBinario para almacenar los elementos
        self.posiciones = {}  # Diccionario para rastrear posiciones de los objetos en el montículo

    def construirMonticulo(self, lista):
        # Recibe una lista de tuplas (clave, objeto) y construye el montículo
        self.monticulo.construirMonticulo(lista)
        for i, (_, obj) in enumerate(self.monticulo.lis_mon[1:], start=1):
            self.posiciones[obj] = i  # Almacena la posición del objeto

    def insertar(self, clave, obj):
        # Inserta una tupla (clave, objeto) en el montículo y actualiza las posiciones
        self.monticulo.insertar((clave, obj))
        self.posiciones[obj] = self.monticulo.tam

    def eliminarMin(self):
        # Extrae el elemento con la mínima clave y actualiza las posiciones
        clave, obj = self.monticulo.eliminarMin()
        self.posiciones.pop(obj, None)
        return clave, obj

    def decrementarClave(self, obj, nueva_clave):
        # Decrementa la clave del objeto y ajusta el montículo
        index = self.posiciones.get(obj)
        if index is not None and nueva_clave < self.monticulo.lis_mon[index][0]:
            self.monticulo.lis_mon[index] = (nueva_clave, obj)  # Actualiza la clave en la posición actual
            self.monticulo.infiltArriba(index)  # Ajusta hacia arriba
            # Actualiza la posición del objeto en el diccionario de posiciones
            self.posiciones[obj] = index

    def estaVacia(self):
        return self.monticulo.tam == 0

    def contiene(self, item):
        # Si tu montículo es una lista de tuplas, por ejemplo [(distancia, vertice)]
        return any(vertice == item for _, vertice in self.monticulo)